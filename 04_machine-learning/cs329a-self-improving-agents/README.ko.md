# CS329A: Self-Improving AI Agents

[English](README.md) | 한국어

스탠퍼드 [CS329A](https://cs329a.stanford.edu/) (2025 가을학기, Aakanksha Chowdhery, Azalia Mirhoseini)를 혼자 공부하기 위한 안내 페이지입니다.

스탠퍼드와 관계없는 비공식 페이지이며, 링크만 모아 두었습니다. 영상, 논문, 수업 자료의 권리는 각 저작권자에게 있습니다.

## 영상

- [Stanford Online 재생목록](https://www.youtube.com/playlist?list=PLangBM27OtEA): 강의 9개, 약 10시간
- [Aakanksha Chowdhery의 2025 겨울학기 재생목록](https://www.youtube.com/playlist?list=PL3058ht9NqT1NG6Y663elpHSDh-AW1TIr): [Lecture 1](https://www.youtube.com/watch?v=EZ-QwlHFt6s), [Lecture 2](https://www.youtube.com/watch?v=uTtDCfGeyiU), [Lecture 3](https://www.youtube.com/watch?v=hgOblXLnUqQ), 아래 초청 강연

## 공식 숙제

수업의 [GitHub 계정](https://github.com/stanford-cs329a)에 공개된 자료입니다.

| 숙제 | 내용 | 필요한 것 | 라이선스 |
|---|---|---|---|
| [숙제 1 (2025 가을)](https://github.com/stanford-cs329a/cs329a-homework1-fall2025-public) | AIME25: Zero-shot, 다수결, Best-of-N, 실행 결과로 고치기 | Together API 키, Hugging Face 토큰 | MIT |
| [숙제 2 (2025 가을)](https://github.com/stanford-cs329a/cs329a-homework2-fall2025-public) | HumanEval: pass@K, LLM 심판, 단위 테스트를 약한 검증자로 쓰기 | Together API 키, Docker | 표시 없음 |
| [숙제 3 (2025 가을)](https://github.com/stanford-cs329a/cs329a-homework3-fall2025-public) | API 라우팅, 질문 쪼개기, 자기 수정, 딥 리서치 에이전트 | Together, Google, Polygon 등 API 키 | Apache-2.0 |

2025 겨울학기 판: [숙제 1](https://github.com/stanford-cs329a/homework1-public-win2025), [숙제 2](https://github.com/stanford-cs329a/cs329-homework2-win2025)

## 계획

주 4~5시간씩 11주 과정입니다. 맞는 주제는 공식 숙제로, 나머지는 직접 정한 실습으로 채웁니다.

| 주 | 영상 | 먼저 읽을 논문 | 실습 |
|---|---|---|---|
| 1 | [Part 1: Course Overview](https://www.youtube.com/watch?v=6YnLB0XbTnI) (1:10) | - | 숙제 1 환경 준비와 1번(Zero-shot) |
| 2 | [Part 2: Test-Time Compute Scaling](https://www.youtube.com/watch?v=-Ggc37xLj_Y) (1:03) | [Large Language Monkeys](https://arxiv.org/abs/2407.21787), [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314) | 숙제 1의 2~3번(다수결, Best-of-N) |
| 3 | [Part 3: Robust Verification](https://www.youtube.com/watch?v=p7TdPUcPoik) (1:13) | [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168), [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | 숙제 2의 1~2부(pass@K, LLM 심판) |
| 4 | [Part 4: Learning from Feedback with Tools/Code](https://www.youtube.com/watch?v=Lxh9RF5S-K0) (1:11) | [ReAct](https://arxiv.org/abs/2210.03629), [RLEF](https://arxiv.org/abs/2410.02089) | 숙제 1의 4번과 분석(실행 결과로 고치기) |
| 5 | [Part 5: Planning and Multi-Step Reasoning](https://www.youtube.com/watch?v=Ml_fp9XkB8Y) (1:15) | [ADaPT](https://arxiv.org/abs/2311.05772), [Language Agent Tree Search (LATS)](https://arxiv.org/abs/2310.04406) | 숙제 2의 3부(단위 테스트를 약한 검증자로 쓰기) |
| 6 | [Part 6: Train Time Scaling/Scaling RL](https://www.youtube.com/watch?v=yVnmHSAy3ck) (1:13) | [STaR](https://arxiv.org/abs/2203.14465), [DeepSeekMath](https://arxiv.org/abs/2402.03300) | 직접 정한 실습: 작은 모델을 강화학습으로 학습 (GPU가 없으면 논문만) |
| 7 | [Part 7: Self-Improvement and Deep Research Agents](https://www.youtube.com/watch?v=Uni9dqyuuDM) (1:12) | [Search-o1](https://arxiv.org/abs/2501.05366), [AlphaCode 2 Technical Report](https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf) | 숙제 3의 0~2부(API 라우팅, 질문 쪼개기, 자기 수정) |
| 8 | [Part 8: Agentic Evaluations and Long Horizon Tasks](https://www.youtube.com/watch?v=8JAqLnTaZu4) (1:15) | [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499), [GDPval](https://arxiv.org/abs/2510.04374) | 숙제 3의 3~4부(에이전트 흐름, 딥 리서치 에이전트) 후 성공률, 비용, 시간 재기 |
| 9 | [Guest: Jeff Clune, Open-ended Agent Learning (Winter 2025)](https://www.youtube.com/watch?v=EZBuPfu85b8) | [The AI Scientist](https://arxiv.org/abs/2408.06292), [AlphaEvolve](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf) | 직접 정한 실습: 평가 결과를 보고 에이전트가 자기 프롬프트를 고치게 하기 |
| 10 | [Guest: Michele Catasta, Coding Agents (Winter 2025)](https://www.youtube.com/watch?v=a0iOk3xrHNc) | [MemGPT](https://arxiv.org/abs/2310.08560), [CodeMonkeys](https://arxiv.org/abs/2501.14723) | 직접 정한 실습: 메모리를 넣고 점수가 오르는지 보기 |
| 11 | [Part 9: Future Research Areas](https://www.youtube.com/watch?v=AyO6wyu4DEg) (1:08), [Denny Zhou, CS25: Large Language Model Reasoning](https://www.youtube.com/watch?v=ebnX5Ur1hBk) | - | 직접 정한 실습: 전체 정리, 유전체 과제 하나에 적용 |

## 주제별 논문

[수업 일정](https://cs329a.stanford.edu/)에 실린 목록입니다.

| 주제 | 논문 |
|---|---|
| Test-time Compute Scaling | [Large Language Monkeys](https://arxiv.org/abs/2407.21787), [Archon](https://arxiv.org/abs/2409.15254), [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314), [How Do Large Language Monkeys Get Their Power (Laws)?](https://arxiv.org/abs/2502.17578) |
| Robust Verification | [Shrinking the Generation-Verification Gap with Weak Verifiers](https://arxiv.org/abs/2506.18203), [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168), [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050), [Math-Shepherd](https://arxiv.org/abs/2312.08935) |
| Learning from Feedback with Tools/Code | [ReAct](https://arxiv.org/abs/2210.03629), [RLEF](https://arxiv.org/abs/2410.02089), [Constitutional AI](https://arxiv.org/abs/2212.08073) |
| Multi-step Reasoning/Planning | [SWiRL](https://arxiv.org/abs/2504.04736), [Language Agent Tree Search (LATS)](https://arxiv.org/abs/2310.04406), [SPRINT](https://arxiv.org/abs/2506.05745), [ADaPT](https://arxiv.org/abs/2311.05772), [Wider or Deeper?](https://arxiv.org/abs/2503.04412) |
| Train Time Scaling/Scaling RL | [STaR](https://arxiv.org/abs/2203.14465), [DeepSeekMath](https://arxiv.org/abs/2402.03300), [DAPO](https://arxiv.org/abs/2503.14476) |
| Open-Ended Evolution of Self-Improving Agents | [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435), [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954), [The AI Scientist](https://arxiv.org/abs/2408.06292), [AlphaEvolve](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf) |
| Self-Improvement with Search & Deep Research Agents | [AlphaCode](https://arxiv.org/abs/2203.07814), [AlphaCode 2 Technical Report](https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf), [Search-o1](https://arxiv.org/abs/2501.05366) |
| Agentic Frameworks for Software Engineering | [CodeMonkeys](https://arxiv.org/abs/2501.14723), [KernelBench](https://arxiv.org/abs/2502.10517), [Improving Parallel Program Performance with LLM Optimizers](https://arxiv.org/abs/2410.15625) |
| Augmenting Agents with Memory | [Cartridges](https://arxiv.org/abs/2506.06266), [MemGPT](https://arxiv.org/abs/2310.08560), [CacheBlend](https://arxiv.org/abs/2405.16444) |
| Agentic Evaluations & Long-Horizon Tasks | [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499), [GDPval](https://arxiv.org/abs/2510.04374), [DeepScholar-Bench](https://arxiv.org/abs/2508.20033) |

수업 일정에는 `arXiv:2505.22954`가 "Automated design of agentic systems"로 적혀 있지만, 실제 링크는 Darwin Gödel Machine 논문입니다. 위 표에는 둘 다 넣었습니다.

## 이전 학생 프로젝트

[2025 겨울학기 프로젝트 페이지](https://cs329a.stanford.edu/pastprojects.html)에 실린 자료입니다.

- AppBench: [report](https://cs329a.stanford.edu/winter2025projects/appbench.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/appbenchposter.pdf)
- PRIME: [report](https://cs329a.stanford.edu/winter2025projects/prime.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/primeposter.pdf)
- Enhancing Mathematical Reasoning: [report](https://cs329a.stanford.edu/winter2025projects/enhancing.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/enhancingposter.pdf)
- Towards Effective Meta-Agents: [report](https://cs329a.stanford.edu/winter2025projects/batu.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/batuposter.pdf)
- ARCHON Augmented: [report](https://cs329a.stanford.edu/winter2025projects/archon.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/archonposter.pdf)

## 비공식 공부 노트

수업이 아니라 다른 학습자가 만든 자료입니다. 내용이 맞는지는 확인하지 않았습니다.

- [onehr/cs329-notes](https://github.com/onehr/cs329-notes)
- [walkinglabs/self-improving-agent-notebook](https://github.com/walkinglabs/self-improving-agent-notebook)

## 공개된 곳을 찾지 못한 자료

슬라이드, 2025 가을학기 초청 강연 대부분.
