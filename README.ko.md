# Seodanggae (서당개)

[English](README.md) | 한국어

<p align="center">
  <img src="assets/banner.svg" width="100%" alt="서당 앞마당을 돌아다니고 앉아 있다가 뒹구는 강아지의 픽셀아트" />
</p>

> 서당개 삼 년이면 풍월을 읊는다.

유전체 분석, 통계, 프로그래밍, AI를 공부하며 정리한 글과 실습 노트북을 모아 두는 저장소입니다.
주제마다 정리 글(`notes.md`)과 실습(`lab.ipynb`)이 한 폴더에 있습니다.

## 분류

| 폴더 | 내용 |
|---|---|
| [01_programming](01_programming/) | Python, R, Linux, Git |
| [02_statistics](02_statistics/) | 기초 통계, 회귀, 생존 분석, 다중 검정 |
| [03_genomics](03_genomics/) | NGS, 변이, copy number, signature, RNA-seq |
| [04_machine-learning](04_machine-learning/) | 머신러닝, 딥러닝, LLM |
| [05_workflow-hpc](05_workflow-hpc/) | Nextflow, Slurm, Docker |

## 폴더 구조

주제마다 폴더를 하나 만들고, 정리 글과 실습을 함께 둡니다.

```text
03_genomics/
├── README.md            주제 목록
└── variant-calling/
    ├── notes.md         정리 글 (또는 notes.html)
    ├── lab.ipynb        실습
    └── data/            실습 데이터 (GitHub에 올라가지 않음)
```

## 새 주제 추가

1. `_template` 폴더를 복사해 분류 폴더 안에 붙여 넣고, 주제 이름으로 바꿉니다.
2. `notes.md`와 `lab.ipynb`를 채웁니다.
3. 분류 폴더의 `README.md` 목록에 한 줄 추가합니다.

폴더 이름은 영어 소문자와 `-`로 씁니다. 주소가 깨지지 않습니다.

## 올리기 전 확인

- [ ] 환자 데이터, EGA 자료, 샘플 ID, 발표 전 결과가 없다.
- [ ] 노트북 출력에 서버 주소, 내부 경로, 토큰이 없다.
- [ ] 교재나 강의 자료를 그대로 옮기지 않았다.

실습은 공개 데이터나 예시 데이터로 합니다.
