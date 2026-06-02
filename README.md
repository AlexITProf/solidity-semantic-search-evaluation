# Function-Level vs Contract-Level Chunking for Semantic Search in Solidity
![Status](https://img.shields.io/badge/Data%20Forge-Week%204-blue)
![Language](https://img.shields.io/badge/Python-3.11-green)
![Domain](https://img.shields.io/badge/Web3-Solidity-orange)

**Author:** AlexIT  
**Competition:** Data Forge — Week 4 (June 2026)  
**Focus:** Practical comparison of chunking strategies and state-of-the-art embedding models on real Solidity DeFi codebases.

## Overview

Solidity smart contracts have a unique structure: short functions, heavy boilerplate, modifiers, events, and NatSpec documentation. Traditional keyword search (grep/BM25) struggles with semantically similar implementations across projects (e.g., different versions of ReentrancyGuard, safeTransfer logic, or flash loan fee calculations).

This research evaluates how different chunking approaches and modern embedding models perform specifically on Solidity code.

This project was created for the Data Forge Week 4 competition and explores practical retrieval techniques for Solidity smart contracts used in modern Web3 systems.

## Key Contributions

- Custom ground-truth dataset of **25 real-world audit-style queries**.
- Comparison of three chunking strategies: **Function-level**, **Contract-level**, and **Hybrid**.
- Evaluation of leading models in 2026:
  - **Voyage-code-3** (specialized code model)
  - **Jina Code Embeddings**
  - **OpenAI text-embedding-3-large** (strong baseline)

## Methodology

### Data Sources
- **OpenZeppelin Contracts** v5.6.1 (industry standard)
- **Aave V3 Core** (complex DeFi protocol)

### Chunking Strategies
1. **Function-level** — Each function + NatSpec + signature + modifiers (recommended)
2. **Contract-level** — Entire contract as one chunk
3. **Hybrid** — Function + surrounding contract context (~250 tokens)

### Models
- Voyage-code-3
- Jina Code Embeddings (latest variant)
- OpenAI text-embedding-3-large

### Evaluation Metrics
- Recall@5, Recall@10
- MRR (Mean Reciprocal Rank)
- NDCG@10

### Evaluation Plan

The project evaluates:
- Recall@5
- Recall@10
- MRR
- NDCG@10

across multiple embedding models and chunking strategies.

### Expected Outcomes

Based on prior research in code retrieval and RAG systems, function-level chunking is expected to outperform contract-level chunking due to improved semantic granularity.

Hybrid retrieval approaches combining BM25 and vector search are also expected to improve ranking quality.

## Future Work

- Full evaluation on OpenZeppelin and Aave V3.
- Comparison of embedding models.
- Hybrid retrieval experiments.
- Reranking evaluation.

## Repository Structure

```text
solidity-semantic-search-evaluation/
├── README.md
├── data/
│   ├── queries.csv
│   ├── extracted_chunks_examples.json
│   └── results_summary.csv
├── src/
│   ├── parser.py
│   ├── embed.py
│   └── eval.py
└── requirements.txt
```

## References
- OpenZeppelin: https://github.com/OpenZeppelin/openzeppelin-contracts
- Aave V3: https://github.com/aave/aave-v3-core
  

**License:** MIT
