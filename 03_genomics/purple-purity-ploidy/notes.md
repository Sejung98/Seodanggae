# PURPLE: purity, ploidy, copy number 맞추기

공부한 날짜:
참고 자료:

- PURPLE 설명서와 소스 코드: [hmftools 태그 purple-v4.1](https://github.com/hartwigmedical/hmftools/tree/purple-v4.1/purple)
- 입력을 만드는 도구: [AMBER v4.1](https://github.com/hartwigmedical/hmftools/blob/amber-v4.1/amber/README.md) (BAF), [COBALT v2.0](https://github.com/hartwigmedical/hmftools/blob/cobalt-v2.0/cobalt/README.md) (깊이 비)
- 논문: Priestley 2019 *Nature* (PURPLE), Van Loo 2010 *PNAS* (ASCAT), Carter 2012 *Nat Biotechnol* (ABSOLUTE), Benjamini & Speed 2012 *NAR*·Aird 2011 *Genome Biol* (GC 편향), Nilsen 2012 *BMC Genomics* (PCF), Dentro 2021 *Cell* (NRPCC), Favero 2015 *Ann Oncol* (Sequenza)
- 노트북마다 맨 끝 `출처` 절에 링크와 "어느 주장에 썼는지"를 적었습니다. 설명서와 코드가 다른 곳은 코드를 따르고 그 사실을 적었습니다.

실습 데이터는 모두 직접 만든 가짜 데이터입니다. 실제 샘플 결과는 `data/`에만 두고 올리지 않습니다.

`purple_mini.py`는 PURPLE 4.1 소스(태그 `purple-v4.1`)의 맞추기 식을 공부용으로 줄여 옮긴 모듈입니다. 가짜 종양 만들기, 구간 나누기, purity·ploidy 맞추기, 다듬기, QC 계산이 들어 있고 노트북 네 개가 이것을 불러 씁니다. 함수마다 어느 Java 파일에서 왔는지와 무엇을 줄였는지 적어 두었습니다. 노트북은 이 파일과 같은 폴더에서 열어야 합니다.

## 왜 공부했나

purity가 낮을수록 왜 CN이 흔들리는지 알고 싶어서.

## 진도

| | 주제 | 실습 | 끝낸 날 |
|---|---|---|---|
| B0 | read 에서 copy 수까지: 세포·DNA 조각, library 와 paired-end, FASTQ 와 염기 품질, 정렬과 MAPQ, pileup 과 깊이, 깊이 잡음과 1 kb 창(짝 read 포함), 깊이로 copy 수 세기와 자리 효과 지우기(정상 시료로 나누기 vs COBALT 의 시료별 GC 보정, PURPLE 은 종양 GC ratio 로 맞춤), 이형접합 SNP 에서 BAF 세기, 중복·반복·SV 단서, COBALT·AMBER 가 만드는 것 | `lab00_reads-to-copies.ipynb` | |
| B1 | 기초 개념(read·깊이, purity, CN·major/minor·ploidy, normFactor, GC 편향과 COBALT 보정, 이형접합 SNP·BAF·접힌 BAF, NRPCC)과 purity 가 낮을 때 신호가 줄어드는 정도, 가짜 데이터 만들기 | `lab01_signal-model.ipynb` | |
| B2 | 맞추기 구현: purity와 깊이 보정값 격자 탐색, 구간별 CN 추정, 벌점, purity 범위 | `lab02_fit.ipynb` | |
| B3 | 낮은 purity 에서 CN 이 흔들리는 네 가지 이유: 1/p 잡음, BAF 바닥, 가짜 구간과 CN noise 경고, 두 배 해로 뒤집힘. SNV VAF 로 확인하기 | `lab03_hard-cases.ipynb` | |
| B4 | 실제 출력 읽기: `purity.tsv`, `purity.range.tsv`, `segment.tsv`, `cnv.somatic.tsv`, `qc`. 시료 확인 함수, 내 결과에 돌리기(선택) | `lab04_outputs.ipynb` | |

## 핵심 내용

### B1. 신호 기초

### B2. 맞추기

### B3. 어려운 경우

### B4. 실제 출력

## 막힌 곳과 해결

## 더 볼 것
