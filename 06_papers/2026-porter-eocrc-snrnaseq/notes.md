# Porter et al. 2026 · Nature Medicine — EO-CRC snRNA-seq atlas

공부한 날짜: 2026-11-10
논문: Porter CBM, …, Xavier RJ, Anderson AC, Ng K. *Insights into early-onset colorectal cancer from a single-nucleus RNA-seq atlas of colorectal cancer across the age continuum.* Nature Medicine (2026). [doi:10.1038/s41591-026-04721-y](https://doi.org/10.1038/s41591-026-04721-y) · PMID 42957776
데이터: snRNA-seq raw dbGaP phs004493.v1.p1, processed GEO GSE312983 / DFCI EO-CRC bulk dbGaP phs004807.v1, GEO GSE333907
분류: Early-onset cancer · Tumor microenvironment · Single-cell methods

> 그림은 넣지 않고 원문 링크로 대신한다. 아래 글은 내 요약과 비평이다.

## 1. 한 줄 요약과 차별점

**한 줄 요약.** 189개 primary CRC(EO 54 / AO 135) snRNA-seq에서, 젊은 MSS 종양은 stroma가 많고 상피가 적다(bulk·조직 영상으로 재현). 젊은 종양 상피에서는 lncRNA와 FN1이 높고, left-sided MSS EO-CRC에서는 EMT 계열 세포 간 신호(FN1/GDF/ACTIVIN/SPP1)가 강하다. 반면 상피 subset 구성, CNA 패턴, 핵심 gene program은 나이와 무관하게 보존된다.

**차별점**

- **Age를 연속변수로 모델링**(z-scored age). 50세 cutoff에 기대지 않고 20대–90+ 8개 decade를 한 축으로 본다.
- **MSI 층화 + sidedness·stage·sex·neoadjuvant 보정을 거의 모든 분석에 적용.** 선행 연구의 약점(작은 EO 표본, 가변 cutoff, panel/bulk, 보정 부재)을 겨냥한다. 예: Cercek 2021에서는 MSI·sidedness 보정 후 genomic 차이가 사라졌고, Willauer 2019는 보정 없이 CMS를 비교했다.
- **냉동 biobank 조직의 snRNA-seq.** stromal nuclei가 47,712개로 기존 CRC scRNA atlas(Pelka 2021)보다 많고, 핵에 머무는 lncRNA를 잡기에 유리하다(Cabili 2015).
- **3중 validation.** bulk deconvolution(564 MSS), NHS/HPFS multispectral IF(712 MSS), 정상 노화 대조(GTEx, TCGA adjacent normal).
- 저자 스스로 **hypothesis-generating**이라고 규정한다. 기능 실험은 없다.

**스토리 한눈에**

1. **출발점.** EO-CRC가 생물학적으로 다른지는 아직 불분명하다. 그래서 189개 종양을 snRNA-seq하고 나이를 연속축으로 본다.
2. **Fig. 1 — 지도.** 세포 종류와 상태는 기존 CRC와 같고, 나이로는 갈리지 않는다.
3. **Fig. 2 — 첫 발견.** 젊은 MSS 종양은 stroma가 많고 상피가 적다. 외부 두 코호트에서도 같은 방향이다.
4. **Fig. 3–4 — 암세포 자체는?** CNA 패턴과 핵심 gene program은 나이와 무관하다.
5. **Fig. 5 — 유전자 단위.** 젊은 종양 상피에서 lncRNA와 FN1이 높다.
6. **Fig. 6 — 세포 간 신호.** 젊은 종양에서 EMT·혈관신생 신호가 많다. 결론은 ‘stroma가 많고 EMT 쪽으로 기운 TME’라는 가설이다.

## 2. 코호트·데이터와 분석 프레임

| 데이터 | 규모 (EO / AO) | 용도 |
|---|---|---|
| DFCI snRNA-seq atlas (10x 3′ v3.1, frozen) | 189 tumors (54 / 135), 850,222 nuclei | 발견 코호트 |
| └ MSS subset | 134 (45 / 89) | composition, CNA, DEG (age 연속) |
| └ MSI-H subset | 42–43 (9 / 33–34) | 보조 분석 |
| └ Left-sided MSS | cNMF 49 (24 / 25), CellChat 51 (25 / 26) | 공변량을 못 넣는 분석의 범주 비교 |
| Bulk RNA-seq | 564 MSS: TCGA 497 (59 / 438) + DFCI EO-CRC FFPE 67 (67 / 0) | MuSiC deconvolution, DEG 재현 |
| NHS/HPFS TMA multispectral IF | 887 → 712 MSS (18 / 694) | stromal:epithelial ratio 재현 |
| GTEx colon aging / TCGA adjacent normal | — / 48 (7 / 41) | 정상 노화 대조 |

- **임상 특성.** EO-CRC는 left-sided(OR 3.61, 95% CI 1.85–7.04)와 stage IV(OR 2.55, 1.23–5.27)가 많다. sex·MSI·neoadjuvant는 나이와 무관하다.
- **공통 모델.** `~ sidedness + neoadjuvant + sex + stage + age_scaled`. effect size는 age 1 SD당 값이다.
- **부호 규약.** β 또는 log2FC가 음수면 나이가 들수록 감소, 즉 젊은 쪽에서 높다.

## 3. Fig. 1 — 지도 그리기: 나이로는 갈리지 않는 atlas

[원문 Fig. 1](https://www.nature.com/articles/s41591-026-04721-y/figures/1)

**이 단계의 질문.** 이 atlas가 믿을 만한 지도인가? 나이가 전사체를 크게 가르는 축인가?

**방법 — 어떻게 확인했나**

- **왜 single-nucleus인가.** 재료가 snap-frozen biobank 조직이라 세포를 온전히 해리할 수 없다. 약 3 mm² 조각에서 핵만 뽑아 10x 3′ v3.1로 읽었다(Slyper 2020 protocol). 오래 보관된 샘플을 쓸 수 있는 대신, 상피가 과대표집되고(84.9%) 면역세포는 적게 잡히며 핵 전사체(intronic, lncRNA)가 상대적으로 많이 잡힌다.
- **QC.** CellBender로 ambient RNA를 빼고 genes < 200, UMI < 400, mito > 50%, doublet을 걸렀다.
- **2단계 annotation.** 낮은 해상도 Leiden(0.1) + 문헌 signature로 7개 lineage를 나눈 뒤, lineage별로 다시 클러스터링한다.
- **Harmony를 언제, 왜 썼나.** 종양 상피는 환자마다 CNA가 달라 환자별로 뭉친다. 환자를 가로질러 공유되는 상태를 찾으려고 annotation 단계에서만 patient Harmony를 썼다. 보정이 만든 가짜 상태가 아닌지 보려고 보정 전 UMAP에 라벨을 다시 올려 확인했다.
- **악성 판정.** tumor signature(Dohmen 2022) 점수가 상피 전부에서 높아 일괄 malignant로 봤다. 주변 정상 상피는 따로 구분하지 않았다.
- **아형 분류.** CMS는 종양별 pseudobulk에 CMScaller(single-sample), iCMS2/3는 Joanito 2022 gene set으로 점수화하고 공통 모델로 나이 효과를 봤다.

**결과 — 그래프가 말하는 것**

- 상피는 stem-like, colonocyte-like, TA-like, goblet-like, enteroendocrine-like로 나뉘고 기존 CRC atlas와 잘 맞는다.
- UMAP은 환자·MSI·sidedness로 갈리고 EO/AO로는 갈리지 않는다.
- ‘EO에 CMS2가 많다’는 sidedness 보정 후 약해지고, ‘젊을수록 CMS1·iCMS3가 적다’는 보정 후에도 남는다.

**→ 다음 질문.** 전사체 전체로는 나이 신호가 없다. 그렇다면 세포 구성비는 다를까? 이후 분석은 sidedness 보정이 기본이다.

## 4. Fig. 2 — 첫 발견: 젊은 MSS 종양은 stroma가 많고 상피가 적다

[원문 Fig. 2](https://www.nature.com/articles/s41591-026-04721-y/figures/2)

**이 단계의 질문.** 세포 상태가 같더라도 비율은 나이에 따라 다를 수 있다. MSS 134개에서 본다.

**방법 — 어떻게 확인했나**

- **구성비 데이터의 함정.** 비율은 합이 1이라, 하나가 오르면 나머지는 자동으로 내려간다. 세포 종류마다 따로 회귀하면 이 가짜 음의 상관을 각각의 발견으로 착각한다.
- **Dirichlet regression.** 모든 비율을 한 번에 모델링한다. common model은 각 비율을, alternative model은 상피를 reference로 둔 log-ratio를 본다.
- **scCODA.** Bayesian 구성비 모델로, 비상피 세포를 하나씩 돌아가며 reference로 두고도 결론이 같은지 확인했다.
- **Bray–Curtis PCoA.** 가설 없이 구성 차이가 가장 큰 축을 본다.
- **검증 1 — bulk deconvolution.** atlas를 reference로 MuSiC(Wang 2019)을 bulk 564개에 적용하고, `log(stroma/상피) ~ age + 공변량 + dataset`을 회귀했다. 젊은 샘플이 거의 DFCI(FFPE) 하나에서 오므로 dataset과 age가 얽혀 있다.
- **검증 2 — 조직 영상.** NHS/HPFS TMA 712개를 multispectral IF(KRT, ACTA2, FAP, CALD1, CD34, PDPN)와 ML phenotyping으로 분류해 stroma:상피 비율을 구했다. 조직이 남은 환자만 분석되는 selection bias는 전체 4,474명으로 IPW 보정했다. transcriptome과 다른 modality라는 점이 중요하다.

**결과 — 그래프가 말하는 것**

- 젊을수록 상피 비율이 낮고 stroma 비율이 높다(상피–age FDR 3.2×10⁻⁵). 다른 비상피 lineage가 모두 ↓인 것은 같은 신호다.
- 상피 안에서의 비율은 그대로다. 특정 암세포 상태가 아니라 ‘상피 총량’이 줄었다.
- MSI-H에서는 변화가 없다.
- bulk(β = −0.19 per SD age)와 조직 영상(<50세 OR 2.70 vs ≥70세, 1.12–6.51)도 같은 방향이다. 효과는 작다(Spearman ρ = −0.11).

**→ 다음 질문.** 암세포 자체도 다를까? 유전체(CNA)부터 본다. 저자들은 stroma가 많은 TME가 항암제 저항과 연관된다는 문헌(Valkenburg 2018)을 근거로 EO-CRC의 나쁜 예후를 설명할 수 있다고 본다.

## 5. Fig. 3 — 암세포의 유전체: CNA는 나이와 거의 무관하다

[원문 Fig. 3](https://www.nature.com/articles/s41591-026-04721-y/figures/3)

**이 단계의 질문.** 젊은 환자의 암세포는 CNA의 양, 패턴, 종양 내 이질성이 다를까? WGS 없이 snRNA로 추정한다.

**방법 — 어떻게 확인했나**

- **inferCNV의 원리.** 구간이 증폭되면 그 구간 유전자들의 발현이 함께 조금씩 오른다. 유전자를 좌표 순서로 놓고 같은 종양의 비상피 세포 대비 발현을 평활화하면 gain/loss가 드러난다. HMM(i6)으로 상태를 부르고, 해상도는 대략 arm 수준이다.
- **종양 내 이질성.** subcluster mode가 CNA 패턴이 다른 세포 집단을 나눈다. 종양당 ‘CNA subset’ 개수(1–5)를 subclonal 이질성의 대리지표로 쓰고, 검출력 차이는 UMI depth와 상피 nuclei 수로 보정했다.
- **코호트 패턴.** subset을 모아 metacluster를 만들고, patient random effect를 넣은 mixed-effects logistic으로 나이와의 관계를 봤다.
- **대조.** TCGA MSS(cBioPortal) CNA와 비교(positive control)하고, Pelka 2021 정상 조직에서는 CNA가 안 잡히는지 확인했다(negative control).
- **CNA burden.** 종양별 평균 |log2 CNA|를 OLS로 봤다.

**결과 — 그래프가 말하는 것**

- 잘 알려진 CRC CNA(7, 8q, 13q, 20q gain / 8p, 17p, 18q loss)를 재현하고 정상 조직과 분리된다. 방법은 믿을 만하다.
- EO와 AO는 섞여 있다. 패턴도 burden도 나이와 무관하다.
- 젊은 종양에서 CNA subset ≥ 3이 많은 경향(P = 0.056)은 있지만, 해당 종양은 약 10개다.

**→ 다음 질문.** 유전체는 비슷하다. 그렇다면 암세포의 전사 프로그램은? 참고로 ‘EO에서 CNA burden↑’라는 선행 보고(Peng & Zhan 2025, EO 17명, sidedness 미보정)는 재현되지 않았다.

## 6. Fig. 4 — 암세포의 프로그램: 핵심은 공유되고 차이는 주변부에 있다

[원문 Fig. 4](https://www.nature.com/articles/s41591-026-04721-y/figures/4)

**이 단계의 질문.** 클러스터 라벨 없이 보면 EO와 AO 암세포가 하는 ‘일’은 다를까?

**방법 — 어떻게 확인했나**

- **cNMF.** 세포×유전자 행렬을 k개의 프로그램(유전자 가중치)과 세포별 사용량으로 분해한다. 한 세포가 여러 프로그램을 쓸 수 있어 연속적·중첩된 상태를 잡는다. 100번 반복해 안정적인 프로그램만 남기고 k = 10을 골랐다.
- **2단계 설계(Kinker 2020).** 종양마다 따로 cNMF를 돌린 뒤 종양 간 반복되는 metaprogram 5개를 EO, AO 각각 만들고, top-50 유전자의 Jaccard distance로 짝지어 비교했다.
- **left-sided MSS로 제한한 이유.** cNMF는 공변량을 못 넣으므로 교란을 설계 단계에서 줄였다(EO 24 / AO 25). 이 안에서 stage·치료·sex·CMS가 고르게 분포하는지 확인했다.

**결과 — 그래프가 말하는 것**

- 5쌍 중 3쌍(증식, colonocyte·ERBB, 리보솜·대사)은 거의 같다.
- 2쌍은 다르다(EO: Wnt, neuronal / AO: serine hydrolase, keratinization). 유전자 2–7개에 기대는 enrichment라 관찰 수준이다.

**→ 다음 질문.** 큰 그림은 같다. 나이에 따라 연속적으로 변하는 개별 유전자는 있을까?

## 7. Fig. 5 — 유전자 단위: 젊은 종양 상피는 lncRNA와 FN1이 높다

[원문 Fig. 5](https://www.nature.com/articles/s41591-026-04721-y/figures/5)

**이 단계의 질문.** 나이에 따라 연속적으로 변하는 유전자가 있고, 그것이 정상 노화가 아니라 종양의 특징일까?

**방법 — 어떻게 확인했나**

- **pseudobulk.** 세포를 표본으로 보면 같은 환자의 세포 수천 개가 독립 표본처럼 계산돼 가짜 양성이 쏟아진다(Squair 2021). subset마다 종양별로 count를 합쳐 종양 하나를 표본 하나로 했다.
- **모델.** DESeq2 `~ sidedness + neoadjuvant + sex + stage + age_scaled`, Wald, FDR < 0.05. log2FC는 age 1 SD당 변화다.
- **lncRNA enrichment.** DEG 중 lncRNA 비율을 Fisher test로 봤다. clone 이름 유전자(AC….1 등)를 일괄 lncRNA로 넣은 점은 주의.
- **대조.** bulk 564개 재현, GTEx 대장 노화 유전자와 TCGA 정상 조직의 나이 DEG와 비교.

**결과 — 그래프가 말하는 것**

- 상피에서 ‘젊은 쪽 ↑’ 유전자가 훨씬 많다(215 vs 44). 주로 stem-like, TA-like, colonocyte-like.
- 세 상태 공통으로 젊은 쪽이 높은 것은 **FN1**(fibronectin, EMT 때 늘어나는 기질 단백질; Kalluri & Weinberg 2009)과 lncRNA 여러 개다.
- ‘젊은 쪽 ↑’ 유전자의 30–45%가 lncRNA이고 stem-like에서 가장 뚜렷하다(OR 3.4). 저자들은 lncRNA가 주로 핵에 있어(Cabili 2015) snRNA-seq가 처음 잡았다고 본다.
- bulk에서 19개가 같은 방향으로 재현됐고(FN1 포함), 정상 노화 유전자와는 거의 겹치지 않는다.

**→ 다음 질문.** FN1은 EMT 과정에서 늘어나는 세포 밖 기질 단백질이다. 세포 사이의 신호 자체도 달라져 있을까?

## 8. Fig. 6 — 세포 간 대화: 젊은 종양에서 EMT·혈관신생 신호가 늘어난다

[원문 Fig. 6](https://www.nature.com/articles/s41591-026-04721-y/figures/6)

**이 단계의 질문.** stroma가 많고 FN1이 높다면 세포 간 신호도 다를까?

**방법 — 어떻게 확인했나**

- **CellChat.** 한쪽 집단의 ligand와 다른 쪽의 receptor(보조인자 포함) 발현으로 통신 확률을 계산하고 permutation으로 유의성을 본다(Jin 2024). pathway별로 합친 information flow를 EO와 AO 사이에서 Wilcoxon으로 비교했다.
- **설정.** 상피는 세부 상태, 나머지는 lineage 단위로 묶었고 10 cells 미만 interaction은 버렸다.
- **한계.** 공변량을 못 넣고 cohort별로 세포를 모아 한 번 돌린다(left-sided MSS, EO 25 / AO 26). 신호를 재는 게 아니라 mRNA로 추론하고, 세포 수가 많은 집단일수록 잘 검출된다. 도구·DB에 따라 결과가 크게 달라진다(Dimitrov 2022).

**결과 — 그래프가 말하는 것**

- EO의 interaction이 약간 많고(2,028 vs 1,908), 증가분은 stroma, myeloid, enteroendocrine-like에서 나온다.
- EO에서 강한 신호는 EMT(FN1, SPP1, GDF, ACTIVIN)와 혈관신생(ANGPT, TENASCIN, SEMA3/6)이다. SPP1과 ACTIVIN은 EO에만 있다.
- AO에서 강한 신호는 JAM, VISFATIN, COLLAGEN, LAMININ이다.

**이야기의 결말.** 젊은 MSS 종양은 암세포 자체는 비슷하고, stroma가 많고 EMT 쪽 신호가 강한 미세환경이 다르다. 다만 interaction 증가는 Fig. 2의 stroma 증가에서 자동으로 따라올 수 있어 독립적인 두 번째 근거로 보기 어렵다.

## 9. Critical appraisal

**요약 판단.** 가장 믿을 만한 것은 ‘MSS에서 젊을수록 stroma↑’(세 modality에서 방향 일관, 효과 작음)와 ‘보존되는 것들’(null + positive control)이다. lncRNA, CNA 이질성, CellChat은 가설 수준이다.

| 주장 | 근거 | 내 판단 |
|---|---|---|
| MSS 젊은 종양 stroma↑ | snRNA Dirichlet + bulk deconvolution + mIF | 중상: 방향 일관, 효과 작음, bulk는 confound |
| 상피 state·CNA 패턴·core program 보존 | Fig. 1, 3, 4 | 중상: positive control 있음 |
| young↑ FN1 | snRNA 3개 subset + bulk | 중 |
| young↑ lncRNA | snRNA DEG + bulk 3개 | 중하: 분류·기술적 축 미배제 |
| CNA 이질성↑ | P = 0.056, 약 10개 종양 | 낮음 |
| EMT signaling↑ | pooled cells, 공변량 없음 | 낮음: composition에 종속 |

1. **Sidedness는 풀 수 없는 문제다(저자 인정).** EO↔left-sided OR 3.61. 보정하면 사라지는 신호(CMS2, iCMS2, CNA burden)가 confounding인지 mediator인지 구분할 수 없다. left-sided only + age 연속 모델을 sensitivity로 같이 보고했어야 한다.
2. **Bulk validation의 dataset–age 공선성(내 지적).** DFCI 67개는 전부 EO이고 FFPE + RiboErase total RNA다. `dataset` 공변량은 평균 이동만 흡수하므로 age 기울기는 사실상 TCGA 내부 EO 59개에 의존하는데, TCGA-only 분석이 없다. total RNA 라이브러리는 핵·non-polyA 전사체를 더 잡으므로 bulk에서 lncRNA↑가 재현된 것이 라이브러리 차이일 가능성도 있다(내 추론). 564개 중 71개는 stroma 추정 0으로 빠졌다.
3. **mIF는 가장 독립적이지만 효과가 작다.** IPW 보정은 강점이지만 ρ = −0.11, <50세는 18명이다. Fig. 2g의 Female OR 0.88 (0.64–2.10)은 CI가 비대칭이라 오타로 보인다.
4. **Composition 결과는 사실상 하나의 신호다.** 6개 비상피 lineage의 ↓는 ‘상피 비율↑’의 다른 표현이다. snRNA는 약 3 mm² 조각에서 나오므로 stroma 비율은 샘플링 위치에 크게 좌우된다.
5. **lncRNA 분류가 느슨하다.** clone 이름 유전자를 전부 lncRNA로 넣었다. novel protein-coding·pseudogene이 섞여 enrichment를 부풀릴 수 있다. decade별 QC는 대체로 비슷해 큰 품질 차이는 없어 보인다.
6. **정상 노화 대조는 검정력이 없다.** TCGA adjacent normal(48개, <50세 7개)에서는 유의 유전자가 하나도 없어 ‘겹침 0’은 아무것도 보여주지 않는다. GTEx 5개, bulk 19개 겹침도 우연 기대치 검정이 없다.
7. **CellChat은 Fig. 2에 종속된다.** 환자 수준 반복이 없고, 세포 수가 많은 집단이 더 잘 검출된다. 총 건수 차이(+6%)는 검정되지 않았다.
8. **CNA 이질성은 소수 종양이 끈다.** 다중비교 보정이 없고 subset 개수가 inferCNV 설정에 의존한다.
9. **보고 방향이 어긋난다.** CMS2 adj. OR 0.68과 CNA subset adj. OR 0.38은 per +1 SD age에서 ‘젊은 쪽↑’로 읽히는데, CMS1 adj. OR 0.36은 본문이 ‘젊은 쪽↓’로 해석한다. Supplementary 확인 필요.
10. **임상 연결은 검증되지 않았다.** ‘stroma↑ → 치료 저항 → 예후 불량’은 다른 문헌에서 빌린 추론이다. NHS/HPFS는 생존 분석에 쓰여 온 코호트인데도(예: Liao 2012) ratio와 예후는 분석하지 않았다.

**강점.** age 연속 설계, 일관된 공변량, pseudobulk DEG, CNA의 negative control, 정직한 limitation 절.

## 10. 조기 발병 유방암(EOBC) 연구에 주는 시사점

모두 내 추론이다.

- **나이와 얽힌 임상 변수.** 이 논문의 sidedness처럼, 유방암에서는 subtype이 나이와 얽힐 수 있다. 보정 모델 옆에 층 내 제한 분석(한 subtype만)을 sensitivity로 나란히 보고하는 형식을 빌려올 만하다.
- **Young-only 코호트의 함정.** 외부 older 코호트(TCGA-BRCA 등)를 붙이면 dataset–age 공선성이 그대로 재현된다. 결론은 within-cohort 분석에서 내야 한다.
- **Purity/stroma 보정.** 나이가 stroma 비율과 연관된다면 bulk 기반 antigen presentation·IFN-γ score는 purity 보정 없이 나이 효과와 섞인다.
- **재사용할 템플릿.** DESeq2 `~ subtype + stage + ... + age_scaled`와 Dirichlet composition 모델.
- **Null을 읽는 법.** CNA 패턴 null은 positive control이 있어 의미가 있고, TCGA normal ‘겹침 0’은 positive control이 없는 null이다.

## 참고문헌 (PubMed 확인)

- Porter CBM et al. *Nat Med* 2026. PMID 42957776. [doi:10.1038/s41591-026-04721-y](https://doi.org/10.1038/s41591-026-04721-y)
- Cercek A et al. A comprehensive comparison of early-onset and average-onset colorectal cancers. *J Natl Cancer Inst* 2021. PMID 34405229. [doi:10.1093/jnci/djab124](https://doi.org/10.1093/jnci/djab124)
- Willauer AN et al. Clinical and molecular characterization of early-onset colorectal cancer. *Cancer* 2019. PMID 30854646. [doi:10.1002/cncr.31994](https://doi.org/10.1002/cncr.31994)
- Peng T, Zhan Q. Single-cell integration analysis… early-onset colorectal cancer. *NPJ Precis Oncol* 2025. PMID 41254101. [doi:10.1038/s41698-025-01129-8](https://doi.org/10.1038/s41698-025-01129-8)
- Furuhashi S et al. Spatial profiling of cancer-associated fibroblasts of sporadic early onset colon cancer microenvironment. *NPJ Precis Oncol* 2023. PMID 37964075. [doi:10.1038/s41698-023-00474-w](https://doi.org/10.1038/s41698-023-00474-w)
- Pelka K et al. Spatially organized multicellular immune hubs in human colorectal cancer. *Cell* 2021. PMID 34450029. [doi:10.1016/j.cell.2021.08.003](https://doi.org/10.1016/j.cell.2021.08.003)
- Joanito I et al. iCMS epithelial tumor cell states. *Nat Genet* 2022. PMID 35773407. [doi:10.1038/s41588-022-01100-4](https://doi.org/10.1038/s41588-022-01100-4)
- Guinney J et al. The consensus molecular subtypes of colorectal cancer. *Nat Med* 2015. PMID 26457759. [doi:10.1038/nm.3967](https://doi.org/10.1038/nm.3967)
- Slyper M et al. A single-cell and single-nucleus RNA-Seq toolbox for fresh and frozen human tumors. *Nat Med* 2020. PMID 32405060. [doi:10.1038/s41591-020-0844-1](https://doi.org/10.1038/s41591-020-0844-1)
- Cabili MN et al. Localization and abundance analysis of human lncRNAs. *Genome Biol* 2015. PMID 25630241. [doi:10.1186/s13059-015-0586-4](https://doi.org/10.1186/s13059-015-0586-4)
- Kinker GS et al. Pan-cancer single-cell RNA-seq identifies recurring programs of cellular heterogeneity. *Nat Genet* 2020. PMID 33128048. [doi:10.1038/s41588-020-00726-6](https://doi.org/10.1038/s41588-020-00726-6)
- Wang X et al. MuSiC deconvolution. *Nat Commun* 2019. PMID 30670690. [doi:10.1038/s41467-018-08023-x](https://doi.org/10.1038/s41467-018-08023-x)
- Jin S, Plikus MV, Nie Q. CellChat. *Nat Protoc* 2024. PMID 39289562. [doi:10.1038/s41596-024-01045-4](https://doi.org/10.1038/s41596-024-01045-4)
- Valkenburg KC et al. Targeting the tumour stroma to improve cancer therapy. *Nat Rev Clin Oncol* 2018. PMID 29651130. [doi:10.1038/s41571-018-0007-1](https://doi.org/10.1038/s41571-018-0007-1)
- Kalluri R, Weinberg RA. The basics of epithelial-mesenchymal transition. *J Clin Invest* 2009. PMID 19487818. [doi:10.1172/JCI39104](https://doi.org/10.1172/JCI39104)
- Liao X et al. Aspirin use, tumor PIK3CA mutation, and colorectal-cancer survival. *N Engl J Med* 2012. PMID 23094721. [doi:10.1056/NEJMoa1207756](https://doi.org/10.1056/NEJMoa1207756)
- Squair JW et al. Confronting false discoveries in single-cell differential expression. *Nat Commun* 2021. PMID 34584091. [doi:10.1038/s41467-021-25960-2](https://doi.org/10.1038/s41467-021-25960-2)
- Dimitrov D et al. Comparison of methods and resources for cell-cell communication inference. *Nat Commun* 2022. PMID 35680885. [doi:10.1038/s41467-022-30755-0](https://doi.org/10.1038/s41467-022-30755-0)
