# Scientific Language Modeling

A domain-specific NLP system for analyzing scientific papers.
Built on top of RAG, embeddings, and NLP fundamentals.

---

## Why This Project?

General NLP works on any text.
Scientific text is different:
- Structured sections (Abstract, Methods, Results, Discussion)
- Domain-specific vocabulary
- Citation networks
- Claims backed by evidence

This project builds tools specifically for scientific literature.

---

## What It Does

- **Paper Ingestion** — load and parse scientific papers by section
- **Scientific NER** — detect methods, datasets, metrics, and models
- **Paper Similarity** — find semantically related papers
- **Key Claim Extraction** — extract main contributions from abstracts
- **Citation Analysis** — analyze paper relationships

---

## Project Structure

```
scientific-language-modeling/
├── notebooks/
│   ├── 01_paper_ingestion.ipynb
│   ├── 02_scientific_ner.ipynb
│   ├── 03_paper_similarity.ipynb
│   ├── 04_claim_extraction.ipynb
│   └── 05_citation_analysis.ipynb
├── src/
│   ├── ingestion.py
│   ├── ner.py
│   └── similarity.py
├── data/
│   ├── raw/
│   └── processed/
└── README.md
```

---

## Stack

Python · sentence-transformers · FAISS · PyPDF2 · spaCy · pandas · matplotlib

---

## What I Learned

TBD — will be updated after all notebooks are complete.

---

## Author

[Honaxen](https://github.com/Honaxen)