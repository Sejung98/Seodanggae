# Study

English | [한국어](README.ko.md)

Notes and hands-on notebooks from studying genomics, statistics, programming, and AI.
Each topic folder holds a write-up (`notes.md`) and a notebook (`lab.ipynb`).

## Categories

| Folder | Contents |
|---|---|
| [01_programming](01_programming/) | Python, R, Linux, Git |
| [02_statistics](02_statistics/) | Basic statistics, regression, survival analysis, multiple testing |
| [03_genomics](03_genomics/) | NGS, variants, copy number, signatures, RNA-seq |
| [04_machine-learning](04_machine-learning/) | Machine learning, deep learning, LLMs |
| [05_workflow-hpc](05_workflow-hpc/) | Nextflow, Slurm, Docker |

## Layout

Each topic gets its own folder, with the write-up and the notebook side by side.

```text
03_genomics/
├── README.md            topic list
└── variant-calling/
    ├── notes.md         write-up (or notes.html)
    ├── lab.ipynb        notebook
    └── data/            practice data (not pushed to GitHub)
```

## Adding a topic

1. Copy `_template` into a category folder and rename it after the topic.
2. Fill in `notes.md` and `lab.ipynb`.
3. Add a row to the category's `README.md`.

Use lowercase English and `-` for folder names so links stay clean.

## Before pushing

- [ ] No patient data, EGA data, sample IDs, or unpublished results.
- [ ] No server addresses, internal paths, or tokens in notebook output.
- [ ] No textbook or lecture material copied as is.

Practice uses public or example data only.
