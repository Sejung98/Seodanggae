# NMF (음수 없는 행렬 분해): 원리, 왜 생겼나, 직접 써 보기

공부한 날짜:
참고 자료: 노트북마다 끝의 `## 출처` 절. 이 저장소의 [행렬 M5](../linear-algebra-matrices/lab05_svd-nmf.ipynb)(SVD·NMF 맛보기)와 [M3](../linear-algebra-matrices/lab03_least-squares.ipynb)(NNLS)에서 이어집니다.

이 저장소의 노트북은 시뮬레이션 데이터만 씁니다. 실제 데이터로 돌린 사본은 `data/` 에만 두고 올리지 않습니다.

## 왜 공부했나

NMF 를 처음부터 이해하고, mutational signature·발현 프로그램 분석에 직접 응용하려고.

## 진도

| | 주제 | 실습 | 끝낸 날 |
|---|---|---|---|
| N1 | NMF 가 푸는 문제와 왜 생겼나: 재료 × 양, 음수 없음의 뜻, PCA 와 비교, 얼굴 예, 역사 | `lab01_what-nmf-solves.ipynb` | |
| N2 | 알고리즘 직접 짜기: 목적 함수(제곱 오차·KL), 곱셈 갱신, 초기값, 모호함, scikit-learn | `lab02_algorithm.ipynb` | |
| N3 | k 고르기와 안정성: 오차 대 k, consensus·cophenetic·silhouette, 과적합 | `lab03_choosing-k.ipynb` | |
| N4 | mutational signature 처음부터 끝까지: VCF → 96칸, 추출, 코사인 짝 맞추기, NNLS 배정, SigProfilerExtractor 와 차이 | `lab04_mutational-signatures.ipynb` | |
| N5 | 발현 프로그램과 다른 응용: 유전자 × 세포, 정규화, cNMF 의 생각, CN signature | `lab05_expression-programs.ipynb` | |

## 핵심 내용

## 막힌 곳과 해결

## 더 볼 것
