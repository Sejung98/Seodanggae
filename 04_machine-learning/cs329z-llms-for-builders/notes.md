# CS329Z 2강: LLMs for Builders

공부한 날짜:
참고 자료:

- 영상: [Stanford CS329Z Lecture 2](https://youtu.be/Vr1NzH8bT44) (Michael Ryan, 1:17:53)
- 슬라이드: [lecture02.pdf](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf) (176쪽)
- 내려받은 사본은 `data/`에 있습니다(git 제외): 슬라이드, 읽을거리 논문 2편 PDF, context engineering 글 HTML
- 읽을거리: [Attention Is All You Need](https://arxiv.org/abs/1706.03762), [Transformers are RNNs](https://arxiv.org/abs/2006.16236), [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- 수업 페이지: [cs329z.stanford.edu](https://cs329z.stanford.edu/)

스탠퍼드와 관계없는 개인 공부 기록입니다. 강의 자료는 링크와 쪽 번호로만 가리킵니다.

## 왜 공부했나

## 진도

실습은 CPU에서 도는 작은 모델(GPT-2)로 합니다.

| | 영상 | 슬라이드 | 주제 | 실습 | 끝낸 날 |
|---|---|---|---|---|---|
| A1 | 0:00–16:03 | 1–23 | 언어 모델, 샘플링(greedy, top-k, top-p, 온도) | `lab01_sampling.ipynb` | |
| A2 | 16:03–28:27 | 24–60 | 트랜스포머, 셀프 어텐션 | `lab02_attention.ipynb` | |
| A3 | 28:27–36:01 | 61–91 | 어텐션과 순환, linear attention | `lab03_linear-attention.ipynb` | |
| A4 | 36:01–52:30 | 92–118 | 학습: 손실, 사전 학습, SFT, RLHF, RLVR | `lab04_training.ipynb` | |
| A5 | 52:30–1:04:58 | 119–148 | 추론: prefill과 decode, KV 캐시, test-time scaling | `lab05_inference.ipynb` | |
| A6 | 1:04:58–1:17:53 | 149–176 | 구조화 출력, 컨텍스트 엔지니어링, context rot | `lab06_context.ipynb` | |

## 핵심 내용

### A1. 언어 모델과 샘플링

### A2. 트랜스포머와 셀프 어텐션

### A3. 어텐션과 순환, linear attention

### A4. 학습

### A5. 추론

### A6. 구조화 출력과 컨텍스트 엔지니어링

## 막힌 곳과 해결

## 더 볼 것
