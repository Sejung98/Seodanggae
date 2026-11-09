# CS329A: Self-Improving AI Agents

[English](README.md) | 한국어

스탠퍼드 [CS329A](https://cs329a.stanford.edu/) (2025 가을학기, Aakanksha Chowdhery, Azalia Mirhoseini)를 혼자 공부하기 위한 안내 페이지입니다.

스탠퍼드와 관계없는 비공식 페이지이며, 링크만 모아 두었습니다. 영상, 논문, 수업 자료의 권리는 각 저작권자에게 있습니다.

## 영상

- [Stanford Online 재생목록](https://www.youtube.com/playlist?list=PLangBM27OtEA): 강의 9개, 약 10시간
- [Aakanksha Chowdhery의 2025 겨울학기 재생목록](https://www.youtube.com/playlist?list=PL3058ht9NqT1NG6Y663elpHSDh-AW1TIr): [Lecture 1](https://www.youtube.com/watch?v=EZ-QwlHFt6s), [Lecture 2](https://www.youtube.com/watch?v=uTtDCfGeyiU), [Lecture 3](https://www.youtube.com/watch?v=hgOblXLnUqQ), 아래 초청 강연

## 계획

주 4~5시간씩 11주 과정입니다. 수업 숙제가 공개되어 있지 않아 실습은 직접 정했습니다.

| 주 | 영상 | 먼저 읽을 논문 | 실습 |
|---|---|---|---|
| 1 | [Part 1: Course Overview](https://www.youtube.com/watch?v=6YnLB0XbTnI) (1:10) | - | LLM 호출 함수를 만들고 GSM8K로 기준 점수 재기 |
| 2 | [Part 2: Test-Time Compute Scaling](https://www.youtube.com/watch?v=-Ggc37xLj_Y) (1:03) | [Large Language Monkeys](https://arxiv.org/abs/2407.21787), [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314) | 답을 여러 번 뽑을수록 정답이 나올 확률이 어떻게 오르는지 그래프 그리기 |
| 3 | [Part 3: Robust Verification](https://www.youtube.com/watch?v=p7TdPUcPoik) (1:13) | [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168), [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | 다수결과 검증 모델 중 어느 쪽이 답을 더 잘 고르는지 비교 |
| 4 | [Part 4: Learning from Feedback with Tools/Code](https://www.youtube.com/watch?v=Lxh9RF5S-K0) (1:11) | [ReAct](https://arxiv.org/abs/2210.03629), [RLEF](https://arxiv.org/abs/2410.02089) | 프레임워크 없이 ReAct 에이전트 직접 만들기 |
| 5 | [Part 5: Planning and Multi-Step Reasoning](https://www.youtube.com/watch?v=Ml_fp9XkB8Y) (1:15) | [ADaPT](https://arxiv.org/abs/2311.05772), [Language Agent Tree Search (LATS)](https://arxiv.org/abs/2310.04406) | 큰 문제를 쪼개고 실패하면 다시 시도하게 하기 |
| 6 | [Part 6: Train Time Scaling/Scaling RL](https://www.youtube.com/watch?v=yVnmHSAy3ck) (1:13) | [STaR](https://arxiv.org/abs/2203.14465), [DeepSeekMath](https://arxiv.org/abs/2402.03300) | 작은 모델을 강화학습으로 학습 (GPU가 없으면 논문만) |
| 7 | [Part 7: Self-Improvement and Deep Research Agents](https://www.youtube.com/watch?v=Uni9dqyuuDM) (1:12) | [Search-o1](https://arxiv.org/abs/2501.05366), [AlphaCode 2 Technical Report](https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf) | PubMed 검색 에이전트를 만들고 인용한 PMID가 실제 있는지 검사 |
| 8 | [Part 8: Agentic Evaluations and Long Horizon Tasks](https://www.youtube.com/watch?v=8JAqLnTaZu4) (1:15) | [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499), [GDPval](https://arxiv.org/abs/2510.04374) | 7주차 에이전트의 성공률, 비용, 시간 재기 |
| 9 | [Guest: Jeff Clune, Open-ended Agent Learning (Winter 2025)](https://www.youtube.com/watch?v=EZBuPfu85b8) | [The AI Scientist](https://arxiv.org/abs/2408.06292), [AlphaEvolve](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf) | 평가 결과를 보고 에이전트가 자기 프롬프트를 고치게 하기 |
| 10 | [Guest: Michele Catasta, Coding Agents (Winter 2025)](https://www.youtube.com/watch?v=a0iOk3xrHNc) | [MemGPT](https://arxiv.org/abs/2310.08560), [CodeMonkeys](https://arxiv.org/abs/2501.14723) | 메모리를 넣고 점수가 오르는지 보기 |
| 11 | [Part 9: Future Research Areas](https://www.youtube.com/watch?v=AyO6wyu4DEg) (1:08), [Denny Zhou, CS25: Large Language Model Reasoning](https://www.youtube.com/watch?v=ebnX5Ur1hBk) | - | 전체 정리, 유전체 과제 하나에 적용 |

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

## 공개된 곳을 찾지 못한 자료

슬라이드, 숙제, 2025 가을학기 초청 강연 대부분.
