# Research Findings: Function-Level Chunking for Solidity Semantic Search

**Author:** AlexIT
**Competition:** Data Forge — Week 4 (June 2026)

---

# Abstract

Modern Web3 applications rely on increasingly complex Solidity codebases. Traditional keyword-based search methods often fail to identify semantically similar implementations when variable names, comments, or code structure differ across projects.

This research explores how chunking strategies influence semantic retrieval quality for Solidity smart contracts and examines the suitability of modern embedding models for Web3-focused Retrieval-Augmented Generation (RAG) systems.

---

# Why Solidity Requires Specialized Retrieval

Unlike traditional application code, Solidity contracts contain:

* Short but highly meaningful functions
* Security-critical modifiers
* NatSpec documentation
* Reusable protocol patterns
* Large amounts of boilerplate

Developers and auditors frequently need to locate logic that is conceptually similar rather than textually identical.

Examples include:

* Reentrancy protection
* Ownership validation
* Token transfer mechanisms
* Flash-loan fee calculations
* Access-control patterns

These use cases make semantic retrieval particularly valuable.

---

# Chunking Strategies

## Contract-Level Chunking

The entire contract is indexed as a single document.

### Advantages

* Full context preserved
* Simple implementation

### Limitations

* Excessive noise
* Reduced retrieval precision
* Large embedding payloads

For large DeFi protocols, a single contract may contain multiple unrelated logical components.

---

## Function-Level Chunking

Each function, modifier, or logical block is embedded independently.

### Advantages

* High semantic precision
* Better retrieval granularity
* Lower token consumption

This approach aligns closely with how auditors and developers reason about smart contracts.

Example targets:

* `nonReentrant`
* `onlyOwner`
* `safeTransfer`
* Fee calculation logic

---

## Hybrid Chunking

Hybrid chunking combines:

* Function-level embeddings
* Additional surrounding context

This preserves local semantic information while maintaining awareness of contract-level relationships.

---

# Embedding Models Considered

## Voyage-code-3

Designed specifically for source code retrieval.

Strengths:

* Strong code understanding
* Large context support
* Optimized retrieval quality

Potential applications:

* Audit assistants
* Solidity RAG systems
* Code similarity search

---

## Jina Code Embeddings

Modern embedding models with strong retrieval performance and efficient deployment options.

Strengths:

* Competitive retrieval quality
* Flexible infrastructure integration
* Suitable for large-scale indexing

---

## OpenAI text-embedding-3-large

A strong general-purpose baseline.

Strengths:

* Broad language support
* Mature ecosystem
* Reliable semantic representations

Limitations:

* Not specifically optimized for Solidity code

---

# Why Hybrid Search Matters

Pure vector search often misses exact identifiers such as:

* Function names
* Error messages
* Contract names
* Protocol-specific terminology

Production systems increasingly combine:

1. BM25 keyword retrieval
2. Vector similarity search
3. Reranking

This approach improves both precision and recall.

---

# Practical Applications

The findings are particularly relevant for:

## Smart Contract Auditing

Finding similar implementations across repositories.

## AI Coding Assistants

Providing relevant Solidity context to LLMs.

## Internal Developer Search

Searching large protocol codebases.

## Vulnerability Research

Locating security-sensitive patterns across projects.

---

# Limitations

This project represents an exploratory evaluation rather than a production benchmark.

Future work should include:

* Larger query datasets
* Additional Solidity repositories
* Expanded model comparisons
* Reranking evaluation
* Vector database benchmarking

---

# Conclusion

Function-level chunking appears to be the most promising strategy for Solidity semantic search due to its alignment with the logical structure of smart contracts.

For production-grade Web3 RAG systems, the most practical architecture is expected to combine:

* Function-level chunking
* Hybrid retrieval (BM25 + vector search)
* Reranking
* Code-specialized embedding models

This combination offers a strong foundation for smart contract auditing, code discovery, and AI-assisted development workflows.
