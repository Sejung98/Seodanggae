"""PURPLE 4.1 의 purity·ploidy 맞추기를 공부용으로 줄여 옮긴 모듈.

원본: github.com/hartwigmedical/hmftools 태그 purple-v4.1 의 purple 모듈.
각 함수 설명에 어느 Java 파일에서 왔는지와 무엇을 줄였는지 적었다.
노트북 lab01~lab04 가 이 파일을 불러 쓴다.
"""
import numpy as np
import pandas as pd
from scipy.stats import binom, norm

# ---------------------------------------------------------------- 상수
# PurpleConstants.java (WGS 기본값)
MIN_PURITY, MAX_PURITY, PURITY_INCREMENT = 0.08, 1.0, 0.01
MIN_PLOIDY, MAX_PLOIDY = 1.0, 8.0
PLOIDY_PENALTY_FACTOR = 0.4          # README 는 0.3 이라 적지만 v4.1 코드 기본값은 0.4
PLOIDY_PENALTY_STANDARD_DEVIATION = 0.05
PLOIDY_PENALTY_MIN_STANDARD_DEVIATION_PER_PLOIDY = 1.5
PLOIDY_PENALTY_SUB_ONE_MAJOR_ALLELE_MULTIPLIER = 1.0
PLOIDY_PENALTY_SUB_MIN_ADDITIONAL = 1.5
PLOIDY_PENALTY_MIN = 0.1             # README 의 0.2 는 targeted 모드 값
MAX_TUMOR_RATIO_TO_FIT = 3.0         # FittedPurityFactory.java
CANDIDATE_PERCENT_RANGE, CANDIDATE_ABS_RANGE = 0.1, 0.0005   # PurityPloidyFitter.java
# AlleleTolerance.java (smoothing)
MAX_DEVIATION_ADJUSTMENT = 0.20
MIN_ABS_CN_TOL, MIN_ABS_CN_ADD = 0.3, 1.0
MIN_REL_CN_TOL, MIN_REL_CN_ADD = 0.12, 0.8
MIN_OBSERVED_BAF_CHANGE = 0.03
# PurpleQCStatus.java
MAX_UNSUPPORTED_SEGMENTS = 220
QC_MIN_PURITY = 0.2

# 시뮬레이션 규모: hg38 상염색체 길이(Mb)를 100 kb 칸으로 나눈다.
CHROM_MB = [248, 242, 198, 190, 181, 171, 159, 145, 138, 134, 135, 133,
            114, 107, 102, 90, 83, 80, 59, 64, 47, 51]
BIN_KB = 100
WINDOWS_PER_BIN = 100                # COBALT 1 kb 창 100 개 = 칸 하나
READ_LEN = 150

# 그림 색 (Okabe-Ito, 색약 안전)
COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#000000"]


# ---------------------------------------------------------------- 1. 앞 방향 모형 (lab01)
def relative_dna(purity, cn):
    """한 위치의 DNA 양 (정상 세포 2 copy 를 2 로 둔 단위)."""
    return purity * cn + 2 * (1 - purity)


def norm_factor(purity, ploidy, average_ratio=1.0):
    """PurityAdjuster.impliedNormFactor: 2*avgRatio / (2 - 2p + ploidy*p)."""
    return 2 * average_ratio / (2 - 2 * purity + ploidy * purity)


def ratio_from_cn(cn, purity, nf):
    """CN 이 정해지면 나오는 깊이 비. PurityAdjuster.impliedAverageRatio 와 같은 꼴."""
    return nf * (1 - purity + cn * purity / 2)


def cn_from_ratio(ratio, purity, nf):
    """PurityAdjuster.purityAdjustedCopyNumber (상염색체, normalRatio = 1)."""
    ratio = np.asarray(ratio, dtype=float)
    return np.where(ratio == 0, 0.0, 2 + 2 * (ratio - nf) / purity / nf)


def expected_baf(purity, major, minor):
    """종양+정상 섞인 시료에서 major 대립유전자 쪽 BAF (접기 전)."""
    return (purity * major + (1 - purity)) / (purity * (major + minor) + 2 * (1 - purity))


def baf_from_observed(observed_baf, purity, cn):
    """PurityAdjuster.purityAdjustedBAFSimple: 관찰 BAF 에서 정상 몫을 빼 종양 BAF 로 되돌림.
    CN <= 1 이면 1 을 돌려준다(원본과 같음)."""
    observed_baf, cn = np.broadcast_arrays(np.asarray(observed_baf, float), np.asarray(cn, float))
    total = purity * cn + 2 * (1 - purity)
    tumor_major = (observed_baf * total - (1 - purity)) / purity
    with np.errstate(divide="ignore", invalid="ignore"):
        out = tumor_major / cn
    return np.where(cn <= 1, 1.0, out)


def nrpcc(depth, purity, ploidy):
    """종양 염색체 한 copy 당 read 수 (number of reads per chromosome copy)."""
    return depth * purity / (purity * ploidy + 2 * (1 - purity))


def ambiguous_baf(average_depth, percent=0.8):
    """ExpectedBAF.expectedBAF: 모호 판정 기준선. 접기 전 Bin(d, 0.5)/d 의 80 백분위를 깊이 d = D/2 .. 1.5D-1 에 걸쳐 평균한 값.
    접은 BAF 로는 대략 60 백분위라 균형 자리의 약 40% 가 이 값보다 높다(위쪽 경계가 아님)."""
    depths = np.arange(average_depth // 2, average_depth * 3 // 2)
    return float(np.mean(binom.ppf(percent, depths, 0.5) / depths))


# ---------------------------------------------------------------- 2. 가짜 종양 만들기 (lab01)
DIPLOID_STATES = [((1, 1), .50), ((1, 0), .15), ((2, 1), .15), ((2, 0), .05),
                  ((2, 2), .05), ((3, 1), .05), ((3, 0), .03), ((4, 1), .02)]
WGD_STATES = [((2, 2), .40), ((2, 1), .15), ((2, 0), .10), ((3, 2), .10),
              ((3, 1), .08), ((4, 2), .07), ((1, 1), .05), ((4, 0), .05)]


def random_profile(seed=1, states=DIPLOID_STATES, breaks_per_chrom=3):
    """염색체마다 무작위로 끊어 (major, minor) 를 붙인 진짜 CN 지도.
    끊긴 자리는 모두 SV 가 받쳐 준다고 둔다."""
    rng = np.random.default_rng(seed)
    probs = np.array([p for _, p in states]); probs /= probs.sum()
    rows = []
    for c, mb in enumerate(CHROM_MB, start=1):
        nbin = mb * 1000 // BIN_KB
        k = rng.poisson(breaks_per_chrom)
        cuts = np.sort(rng.choice(np.arange(20, nbin - 20), size=min(k, 10), replace=False)) if k else []
        edges = [0, *cuts, nbin]
        for s, e in zip(edges[:-1], edges[1:]):
            major, minor = states[rng.choice(len(states), p=probs)][0]
            rows.append(dict(chromosome=str(c), start_bin=int(s), end_bin=int(e), major=major, minor=minor))
    return pd.DataFrame(rows)


def profile_ploidy(profile):
    length = profile.end_bin - profile.start_bin
    return float(np.average(profile.major + profile.minor, weights=length))


def simulate(profile, purity, depth=60, sys_sd=0.03, sys_corr=0.95, white_sd=0.02,
             het_per_bin=30, seed=0):
    """COBALT·AMBER 비슷한 관찰값을 만든다.

    bins: 100 kb 칸마다 깊이 비 (평균 1 로 맞춤)
      - read 세기 잡음: Poisson (깊이에 따라 줄어듦)
      - 계통 잡음: GC 물결을 흉내 낸 이웃끼리 닮은 잡음 (sys_sd, 깊이와 무관)
      - 그 밖의 잡음: 칸마다 독립 (white_sd, 깊이와 무관)
    bafs: 이형접합 SNP 자리마다 접은 BAF (0.5 + |BAF - 0.5|, AMBER 의 tumorModifiedBAF)
    """
    rng = np.random.default_rng(seed)
    seg = profile.loc[profile.index.repeat(profile.end_bin - profile.start_bin)].reset_index(drop=True)
    seg["bin"] = np.concatenate([np.arange(s, e) for s, e in zip(profile.start_bin, profile.end_bin)])
    cn = (seg.major + seg.minor).to_numpy(float)
    rel = relative_dna(purity, cn)
    mean_rel = rel.mean()
    lam = depth * 1000 / READ_LEN * WINDOWS_PER_BIN            # 평균 칸 하나의 read 수
    counts = rng.poisson(lam * rel / mean_rel)
    ar = np.empty(len(cn)); ar[0] = rng.normal()
    eps = rng.normal(size=len(cn))
    for i in range(1, len(cn)):                                # AR(1): 이웃 칸끼리 닮은 잡음
        ar[i] = sys_corr * ar[i - 1] + np.sqrt(1 - sys_corr ** 2) * eps[i]
    ratio = counts / lam * np.exp(sys_sd * ar + white_sd * rng.normal(size=len(cn)))
    bins = pd.DataFrame(dict(chromosome=seg.chromosome, bin=seg.bin, ratio=ratio,
                             true_cn=cn, major=seg.major, minor=seg.minor))
    # BAF 점
    n_het = rng.poisson(het_per_bin, size=len(cn))
    idx = np.repeat(np.arange(len(cn)), n_het)
    b_major = expected_baf(purity, seg.major.to_numpy(float), seg.minor.to_numpy(float))[idx]
    phase = rng.random(len(idx)) < 0.5                          # alt 가 major 쪽인지 minor 쪽인지
    b = np.where(phase, b_major, 1 - b_major)
    d = rng.poisson(depth * (rel / mean_rel)[idx])
    keep = d > 0
    alt = rng.binomial(d[keep], b[keep])
    baf = alt / d[keep]
    bafs = pd.DataFrame(dict(chromosome=seg.chromosome.to_numpy()[idx[keep]], bin=seg.bin.to_numpy()[idx[keep]],
                             baf=0.5 + np.abs(baf - 0.5), depth=d[keep]))
    return bins, bafs


def simulate_snvs(profile, purity, depth=60, n=3000, clonal_mult=1, seed=0, min_alt=3):
    """체세포 SNV. 한 copy 에만 생긴 클론 변이(multiplicity = clonal_mult)를 깔고 read 를 뽑는다.
    alt read 가 min_alt 이상인 것만 '찾은' 변이로 남긴다."""
    rng = np.random.default_rng(seed)
    length = (profile.end_bin - profile.start_bin).to_numpy(float)
    pick = rng.choice(len(profile), size=n, p=length / length.sum())
    cn = (profile.major + profile.minor).to_numpy(float)[pick]
    major = profile.major.to_numpy(float)[pick]
    mult = np.minimum(clonal_mult, np.maximum(major, 1))
    rel = relative_dna(purity, cn)
    mean_rel = relative_dna(purity, profile_ploidy(profile))
    vaf = purity * mult / rel
    d = rng.poisson(depth * rel / mean_rel)
    alt = rng.binomial(d, vaf)
    out = pd.DataFrame(dict(cn=cn, mult=mult, true_vaf=vaf, depth=d, alt=alt))
    out = out[out.alt >= min_alt].copy()
    out["vaf"] = out.alt / out.depth
    return out


# ---------------------------------------------------------------- 3. 구간 나누기 (lab03)
def pcf(y, gamma=40.0):
    """Piecewise constant fit: 구간별 제곱오차 합 + 구간 수 x 벌점 을 최소로 하는 끊김 자리.
    정확한 동적 계획법(O(n^2)). 벌점 = gamma x 잡음 분산 (copynumber 패키지와 같은 생각)."""
    y = np.asarray(y, float); n = len(y)
    sd = 1.4826 * np.median(np.abs(np.diff(y) - np.median(np.diff(y)))) / np.sqrt(2)
    pen = gamma * sd ** 2
    s1 = np.concatenate([[0], np.cumsum(y)]); s2 = np.concatenate([[0], np.cumsum(y * y)])
    best = np.zeros(n + 1); prev = np.zeros(n + 1, int)
    for j in range(1, n + 1):
        i = np.arange(j)
        cost = best[i] + (s2[j] - s2[i]) - (s1[j] - s1[i]) ** 2 / (j - i) + pen
        k = int(np.argmin(cost)); best[j] = cost[k]; prev[j] = k
    cuts, j = [], n
    while j > 0:
        cuts.append(j); j = prev[j]
    return sorted(cuts)[:-1]          # 끝점 n 은 뺀다


def segment(bins, profile=None, gamma=40.0):
    """PCF 끊김 + (있으면) SV 끊김을 합친다. PURPLE 규칙 2: PCF 끊김은 기존 끊김에서
    한 칸 이상 떨어져 있을 때만 넣는다. 반환: 칸마다 구간 번호와 구간 경계의 근거.
    줄인 점: 실제 PURPLE 은 1 kb 깊이 비와 BAF 를 따로 PCF(gamma 100)로 자른다. 여기서는 100 kb 칸의
    log2 깊이 비만 gamma 40 으로 자르고 BAF 는 자르지 않는다."""
    seg_rows = []
    for c, g in bins.groupby("chromosome", sort=False):
        nbin = len(g)
        sv = set()
        if profile is not None:
            p = profile[profile.chromosome == c]
            sv = set(p.start_bin.iloc[1:].tolist())
        cuts = set(sv)
        for b in pcf(np.log2(g.ratio.clip(lower=1e-3)).to_numpy(), gamma):
            if all(abs(b - x) > 1 for x in cuts):
                cuts.add(b)
        edges = [0, *sorted(cuts), nbin]
        for s, e in zip(edges[:-1], edges[1:]):
            seg_rows.append(dict(chromosome=c, start_bin=s, end_bin=e,
                                 start_support="TELOMERE" if s == 0 else ("BND" if s in sv else "NONE"),
                                 end_support="TELOMERE" if e == nbin else ("BND" if e in sv else "NONE")))
    return pd.DataFrame(seg_rows)


def summarize(bins, bafs, segments):
    """PURPLE 의 ObservedRegion 처럼 구간마다 깊이 비 중앙값, 접은 BAF 중앙값, BAF 점 수를 모은다."""
    segs = segments.copy().reset_index(drop=True)
    key = {}
    for i, r in segs.iterrows():
        for b in range(r.start_bin, r.end_bin):
            key[(r.chromosome, b)] = i
    bseg = np.array([key[(c, b)] for c, b in zip(bins.chromosome, bins.bin)])
    fseg = np.array([key[(c, b)] for c, b in zip(bafs.chromosome, bafs.bin)])
    segs["observedTumorRatio"] = pd.Series(bins.ratio.to_numpy()).groupby(bseg).median()
    segs["observedBAF"] = pd.Series(bafs.baf.to_numpy()).groupby(fseg).median()
    segs["bafCount"] = pd.Series(np.ones(len(fseg), int)).groupby(fseg).sum()
    segs["bafCount"] = segs.bafCount.fillna(0).astype(int)
    segs["depthWindowCount"] = (segs.end_bin - segs.start_bin) * WINDOWS_PER_BIN
    segs["true_cn"] = pd.Series(bins.true_cn.to_numpy()).groupby(bseg).mean()
    return segs


def true_segments(profile):
    """SV 가 진짜 끊김을 모두 알려 준다고 둔 구간 (lab02 의 깨끗한 경우)."""
    s = profile[["chromosome", "start_bin", "end_bin"]].copy()
    s["start_support"] = np.where(s.start_bin == 0, "TELOMERE", "BND")
    last = s.groupby("chromosome").end_bin.transform("max")
    s["end_support"] = np.where(s.end_bin == last, "TELOMERE", "BND")
    return s


# ---------------------------------------------------------------- 4. 맞추기 (lab02)
def ploidy_grid(min_ploidy=MIN_PLOIDY, max_ploidy=MAX_PLOIDY):
    """FittedPurityFactory.ploidyRange: 1~3 은 0.02, 3~5 는 0.05, 5~ 는 0.1 간격."""
    out = []
    for lo, hi, step in [(min_ploidy, 3, 0.02), (max(3, min_ploidy), 5, 0.05), (max(5, min_ploidy), max_ploidy, 0.1)]:
        x = lo
        while x < hi - 1e-9:
            out.append(round(x, 2)); x = round(x + step, 2)
    out.append(max_ploidy)
    return np.array(out)


def purity_grid(min_purity=MIN_PURITY, max_purity=MAX_PURITY, step=PURITY_INCREMENT):
    return np.round(np.arange(min_purity, max_purity + 1e-9, step), 2)


def _allele_deviation(purity, nf, acn):
    """PloidyDeviation.alleleDeviation: 정수에서 얼마나 떨어졌나를 '표준편차 몇 개' 로 바꿔 확률로."""
    dist = np.where(acn < -0.5, 0.5, np.abs(acn - np.round(acn)))
    sd_per_ploidy = np.maximum(PLOIDY_PENALTY_MIN_STANDARD_DEVIATION_PER_PLOIDY,
                               purity * nf / 2 / PLOIDY_PENALTY_STANDARD_DEVIATION)
    return 2 * norm.cdf(dist * sd_per_ploidy) - 1 + np.maximum(-0.5 - acn, 0)


def _sub_min_additional(min_ploidy, acn):
    a = PLOIDY_PENALTY_SUB_MIN_ADDITIONAL
    return np.minimum(a, np.maximum(0, -a * (acn - min_ploidy)))


def major_allele_deviation(purity, nf, acn):
    """PloidyDeviation.majorAlleleDeviation."""
    mult = np.where((acn > 0) & (acn < 1),
                    np.maximum(1, PLOIDY_PENALTY_SUB_ONE_MAJOR_ALLELE_MULTIPLIER * (1 - acn)), 1)
    return np.maximum(mult * _allele_deviation(purity, nf, acn) + _sub_min_additional(1, acn), PLOIDY_PENALTY_MIN)


def minor_allele_deviation(purity, nf, acn):
    """PloidyDeviation.minorAlleleDeviation."""
    return np.maximum(_allele_deviation(purity, nf, acn) + _sub_min_additional(0, acn), PLOIDY_PENALTY_MIN)


def event_penalty(major, minor, factor=None):
    """RegionFitCalculator.calculateEventPenalty. factor 를 안 주면 모듈 상수 PLOIDY_PENALTY_FACTOR 를 쓴다."""
    factor = PLOIDY_PENALTY_FACTOR if factor is None else factor
    wgd = 1 + np.abs(major - 2) + np.abs(minor - 2)
    single = np.abs(major - 1) + np.abs(minor - 1)
    return 1 + factor * np.minimum(single, wgd)


def region_fit(purity, nf, ratio, obs_baf, amb_baf):
    """RegionFitCalculator.calculateRegionFit (상염색체만).
    줄인 점 1: 관찰 BAF 가 모호 판정 기준선 이하일 때 원본은 estimateMinMaxBaf 로 정수 해를 먼저 찾고,
    못 찾으면 BAF 0.5 와 관찰값 중 편차가 작은 쪽을 고른다. 여기서는 뒤의 두 후보 비교만 한다.
    줄인 점 2: 그 비교에서 관찰값 쪽이 이기면 원본은 보정 전 관찰 BAF 를 그대로 종양 BAF 로 돌려준다
    (`? BAF_PNT_5 : observedBAF`). 여기서는 purity 로 보정한 값(b_obs)을 쓴다."""
    cn = cn_from_ratio(ratio, purity, nf)
    b_obs = np.clip(baf_from_observed(obs_baf, purity, cn), 0, 1)
    b_half = np.clip(baf_from_observed(0.5, purity, cn), 0, 1)

    def total_dev(b):
        maj = b * cn
        return major_allele_deviation(purity, nf, maj) + minor_allele_deviation(purity, nf, cn - maj)

    use_half = (obs_baf <= amb_baf) & (total_dev(b_half) < total_dev(b_obs))
    b = np.where(use_half, 0.5, b_obs)
    b = np.where(cn <= 0.1, 1.0, b)                     # impliedBaf: CN 이 거의 0 이면 1
    major = b * cn
    minor = cn - major
    dev = (minor_allele_deviation(purity, nf, minor) + major_allele_deviation(purity, nf, major)) * obs_baf
    return dict(cn=cn, baf=b, major=major, minor=minor, deviation=dev, event=event_penalty(major, minor))


def fit(segs, average_depth=60, purities=None, ploidies=None):
    """FittedPurityFactory.fitPurity: purity x ploidy 격자의 모든 칸에 점수를 매긴다.
    ploidy 칸마다 normFactor 는 impliedNormFactor(BAF 가중 평균 깊이 비, purity, ploidy).
    점수 = (BAF 가중 평균 event 벌점) x (BAF 가중 평균 deviation 벌점).
    ploidyGrid 열은 공부용으로 붙인 격자 값이고 PURPLE 출력에는 없다(출력의 ploidy 는 BAF 가중 평균 CN).
    줄인 점: 체세포 SNV 벌점(somatic penalty)은 넣지 않았다."""
    purities = purity_grid() if purities is None else purities
    ploidies = ploidy_grid() if ploidies is None else ploidies
    use = segs[(segs.bafCount > 0) & (segs.observedTumorRatio <= MAX_TUMOR_RATIO_TO_FIT)]
    w = use.bafCount.to_numpy(float); w = w / w.sum()
    r = use.observedTumorRatio.to_numpy(float)[None, :]
    ob = use.observedBAF.to_numpy(float)[None, :]
    avg_ratio = float(np.sum(w * use.observedTumorRatio))
    amb = ambiguous_baf(int(average_depth))
    rows = []
    for p in purities:
        nf = norm_factor(p, ploidies, avg_ratio)[:, None]
        f = region_fit(p, nf, r, ob, amb)
        diploid = (f["major"] >= 0.8) & (f["major"] <= 1.2) & (f["minor"] >= 0.8) & (f["minor"] <= 1.2)
        ev = f["event"] @ w; dv = f["deviation"] @ w
        rows.append(pd.DataFrame(dict(purity=p, ploidyGrid=ploidies, normFactor=nf[:, 0], score=ev * dv,
                                      diploidProportion=diploid @ w, ploidy=f["cn"] @ w,
                                      eventPenalty=ev, deviationPenalty=dv)))
    return pd.concat(rows, ignore_index=True).sort_values("score", ignore_index=True)


def candidates(fits):
    """PurityPloidyFitter.inRangeOfLowest: 최저 점수에서 10% 또는 0.0005 안의 해들."""
    best = fits.score.min()
    diff = (fits.score - best).abs()
    return fits[(diff <= CANDIDATE_ABS_RANGE) | (diff / best <= CANDIDATE_PERCENT_RANGE)]


def summary(fits):
    """purple.purity.tsv 의 핵심 열: 최적해 + 후보 범위."""
    best = fits.iloc[0]; c = candidates(fits)
    return dict(purity=best.purity, normFactor=best.normFactor, score=best.score, ploidy=best.ploidy,
                diploidProportion=best.diploidProportion,
                minPurity=c.purity.min(), maxPurity=c.purity.max(),
                minPloidy=c.ploidy.min(), maxPloidy=c.ploidy.max())


def best_fit_per_purity(fits):
    """FittedPurityRangeFile.bestFitPerPurity: purity 마다 가장 낮은 점수 하나."""
    return fits.sort_values("score").drop_duplicates("purity").sort_values("purity", ignore_index=True)


def apply_fit(segs, purity, nf, average_depth=60):
    """정한 purity, normFactor 로 구간마다 CN 과 major/minor 를 매긴다."""
    f = region_fit(purity, nf, segs.observedTumorRatio.to_numpy(float), segs.observedBAF.fillna(0.5).to_numpy(float),
                   ambiguous_baf(int(average_depth)))
    out = segs.copy()
    out["tumorCopyNumber"] = f["cn"]; out["tumorBAF"] = f["baf"]
    out["majorAlleleCopyNumber"] = f["major"]; out["minorAlleleCopyNumber"] = f["minor"]
    out["deviationPenalty"] = f["deviation"]; out["eventPenalty"] = f["event"]
    return out


# ---------------------------------------------------------------- 5. 다듬기와 QC (lab03, lab04)
def in_tolerance(a, b, purity):
    """AlleleTolerance.inTolerance (refNormalisedCopyNumber 비교는 뺐다: 정상 깊이 비를 1 로 두었으므로 같음)."""
    adj = max(1.0, MAX_DEVIATION_ADJUSTMENT / purity)
    n_baf = min(a.bafCount, b.bafCount)
    if n_baf > 0:
        max_minor_dev = adj * (MIN_ABS_CN_TOL + 0.5 * max(a.tumorCopyNumber, b.tumorCopyNumber) / np.sqrt(n_baf))
        if abs(a.minorAlleleCopyNumber - b.minorAlleleCopyNumber) > max_minor_dev and \
                abs(a.observedBAF - b.observedBAF) > MIN_OBSERVED_BAF_CHANGE:
            return False
    n_dw = min(a.depthWindowCount, b.depthWindowCount)
    abs_tol = adj * (MIN_ABS_CN_TOL + MIN_ABS_CN_ADD / np.sqrt(n_dw))
    rel_tol = adj * (MIN_REL_CN_TOL + MIN_REL_CN_ADD / np.sqrt(n_dw))
    x, y = a.tumorCopyNumber, b.tumorCopyNumber
    d = abs(x - y)
    rel = 0 if d == 0 else (1 if min(x, y) == 0 else d / abs(min(x, y)))
    return d <= abs_tol or rel <= rel_tol


def smooth(fitted, purity):
    """구간 합치기. 원본(ExtendDiploid 등)은 가장 믿을 만한 구간에서 양쪽으로 넓혀 가고,
    작은 '애매한' 구간은 한꺼번에 흡수한다. 여기서는 왼쪽부터 차례로 붙이는 단순한 방식만 쓴다.
    SV 가 받치는 경계는 넘지 않는다 (규칙 1)."""
    out = []
    for _, g in fitted.groupby("chromosome", sort=False):
        cur = None
        for _, r in g.iterrows():
            if cur is not None and r.start_support == "NONE" and in_tolerance(cur, r, purity):
                w1, w2 = cur.depthWindowCount, r.depthWindowCount
                b1, b2 = cur.bafCount, r.bafCount
                cur = cur.copy()
                cur["tumorCopyNumber"] = (cur.tumorCopyNumber * w1 + r.tumorCopyNumber * w2) / (w1 + w2)
                cur["minorAlleleCopyNumber"] = (cur.minorAlleleCopyNumber * w1 + r.minorAlleleCopyNumber * w2) / (w1 + w2)
                cur["majorAlleleCopyNumber"] = cur.tumorCopyNumber - cur.minorAlleleCopyNumber
                if b1 + b2 > 0:
                    cur["observedBAF"] = (np.nan_to_num(cur.observedBAF) * b1 + np.nan_to_num(r.observedBAF) * b2) / (b1 + b2)
                cur["bafCount"] = b1 + b2
                cur["depthWindowCount"] = w1 + w2
                cur["end_bin"] = r.end_bin; cur["end_support"] = r.end_support
            else:
                if cur is not None:
                    out.append(cur)
                cur = r.copy()
        out.append(cur)
    return pd.DataFrame(out).reset_index(drop=True)


def unsupported_segments(smoothed):
    """PurpleSummaryData.createQC: 양쪽 끝 모두 근거가 NONE 인 구간 수."""
    return int(((smoothed.start_support == "NONE") & (smoothed.end_support == "NONE")).sum())


def qc_status(unsupported, purity):
    """PurpleQCStatus.calcStatus 중 두 가지만."""
    s = []
    if unsupported > MAX_UNSUPPORTED_SEGMENTS:
        s.append("WARN_HIGH_COPY_NUMBER_NOISE")
    if purity < QC_MIN_PURITY:
        s.append("WARN_LOW_PURITY")
    return ",".join(s) or "PASS"


# ---------------------------------------------------------------- 6. 체세포 변이로 purity (lab03)
def somatic_purity(snvs, average_depth, bandwidth=0.03):
    """SomaticPurityFitter 의 뼈대: 깊이가 평균의 0.8~1.2 배인 SNV 의 VAF 분포에서
    무게가 충분한 봉우리 가운데 VAF 가 가장 높은 것 x 2.
    줄인 점: 생식세포 거르기, 재조정(readjustment), hotspot 확인은 없다."""
    v = snvs[(snvs.depth > 0.8 * average_depth) & (snvs.depth < 1.2 * average_depth)].vaf.to_numpy()
    if len(v) < 10:
        return np.nan
    grid = np.arange(0.0, 0.5 + 1e-9, 0.005)
    dens = norm.pdf((grid[:, None] - v[None, :]) / bandwidth).sum(1)
    peaks = [i for i in range(1, len(grid) - 1) if dens[i] >= dens[i - 1] and dens[i] > dens[i + 1]]
    weight = lambda i: np.sum(np.abs(v - grid[i]) <= bandwidth)
    ok = [i for i in peaks if weight(i) > max(4, 0.03 * len(v))]
    if not ok:
        return np.nan
    return 2 * grid[max(ok)]
