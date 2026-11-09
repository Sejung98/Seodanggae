# CS329A: Self-Improving AI Agents

English | [한국어](README.ko.md)

My self-study guide to Stanford's [CS329A](https://cs329a.stanford.edu/) (Autumn 2025, Aakanksha Chowdhery and Azalia Mirhoseini).

This is an unofficial page, not affiliated with Stanford. It holds links only. All videos, papers, and course materials belong to their owners.

## Videos

- [Stanford Online playlist](https://www.youtube.com/playlist?list=PLangBM27OtEA): nine lectures, about 10 hours
- [Winter 2025 playlist by Aakanksha Chowdhery](https://www.youtube.com/playlist?list=PL3058ht9NqT1NG6Y663elpHSDh-AW1TIr): [Lecture 1](https://www.youtube.com/watch?v=EZ-QwlHFt6s), [Lecture 2](https://www.youtube.com/watch?v=uTtDCfGeyiU), [Lecture 3](https://www.youtube.com/watch?v=hgOblXLnUqQ), and the guest talks below

## Plan

Eleven weeks at 4 to 5 hours a week. The labs are my own, because the course homework is not public.

| Week | Video | Read first | Lab |
|---|---|---|---|
| 1 | [Part 1: Course Overview](https://www.youtube.com/watch?v=6YnLB0XbTnI) (1:10) | - | LLM call function and a baseline score on GSM8K |
| 2 | [Part 2: Test-Time Compute Scaling](https://www.youtube.com/watch?v=-Ggc37xLj_Y) (1:03) | [Large Language Monkeys](https://arxiv.org/abs/2407.21787), [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314) | Plot how often the right answer appears as samples increase |
| 3 | [Part 3: Robust Verification](https://www.youtube.com/watch?v=p7TdPUcPoik) (1:13) | [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168), [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | Compare majority vote with a verifier for picking answers |
| 4 | [Part 4: Learning from Feedback with Tools/Code](https://www.youtube.com/watch?v=Lxh9RF5S-K0) (1:11) | [ReAct](https://arxiv.org/abs/2210.03629), [RLEF](https://arxiv.org/abs/2410.02089) | Build a ReAct agent without a framework |
| 5 | [Part 5: Planning and Multi-Step Reasoning](https://www.youtube.com/watch?v=Ml_fp9XkB8Y) (1:15) | [ADaPT](https://arxiv.org/abs/2311.05772), [Language Agent Tree Search (LATS)](https://arxiv.org/abs/2310.04406) | Split large problems and retry on failure |
| 6 | [Part 6: Train Time Scaling/Scaling RL](https://www.youtube.com/watch?v=yVnmHSAy3ck) (1:13) | [STaR](https://arxiv.org/abs/2203.14465), [DeepSeekMath](https://arxiv.org/abs/2402.03300) | Train a small model with RL (papers only if no GPU) |
| 7 | [Part 7: Self-Improvement and Deep Research Agents](https://www.youtube.com/watch?v=Uni9dqyuuDM) (1:12) | [Search-o1](https://arxiv.org/abs/2501.05366), [AlphaCode 2 Technical Report](https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf) | PubMed search agent that checks its cited PMIDs exist |
| 8 | [Part 8: Agentic Evaluations and Long Horizon Tasks](https://www.youtube.com/watch?v=8JAqLnTaZu4) (1:15) | [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499), [GDPval](https://arxiv.org/abs/2510.04374) | Measure the week 7 agent's success rate, cost, and time |
| 9 | [Guest: Jeff Clune, Open-ended Agent Learning (Winter 2025)](https://www.youtube.com/watch?v=EZBuPfu85b8) | [The AI Scientist](https://arxiv.org/abs/2408.06292), [AlphaEvolve](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf) | Let the agent revise its own prompt from its evaluation |
| 10 | [Guest: Michele Catasta, Coding Agents (Winter 2025)](https://www.youtube.com/watch?v=a0iOk3xrHNc) | [MemGPT](https://arxiv.org/abs/2310.08560), [CodeMonkeys](https://arxiv.org/abs/2501.14723) | Add memory and see whether the score rises |
| 11 | [Part 9: Future Research Areas](https://www.youtube.com/watch?v=AyO6wyu4DEg) (1:08), [Denny Zhou, CS25: Large Language Model Reasoning](https://www.youtube.com/watch?v=ebnX5Ur1hBk) | - | Wrap up and apply it to one genomics task |

## Reading list by topic

From the [course schedule](https://cs329a.stanford.edu/).

| Topic | Papers |
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

The schedule labels `arXiv:2505.22954` as "Automated design of agentic systems", but that link is the Darwin Gödel Machine paper. Both are listed above.

## Past student projects

From the [Winter 2025 projects page](https://cs329a.stanford.edu/pastprojects.html).

- AppBench: [report](https://cs329a.stanford.edu/winter2025projects/appbench.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/appbenchposter.pdf)
- PRIME: [report](https://cs329a.stanford.edu/winter2025projects/prime.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/primeposter.pdf)
- Enhancing Mathematical Reasoning: [report](https://cs329a.stanford.edu/winter2025projects/enhancing.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/enhancingposter.pdf)
- Towards Effective Meta-Agents: [report](https://cs329a.stanford.edu/winter2025projects/batu.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/batuposter.pdf)
- ARCHON Augmented: [report](https://cs329a.stanford.edu/winter2025projects/archon.pdf), [poster](https://cs329a.stanford.edu/winter2025projects/archonposter.pdf)

## Not found publicly

Slides, homework, and most Autumn 2025 guest lectures.
