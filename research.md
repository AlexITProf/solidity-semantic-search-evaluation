# Research Findings: Function-Level vs Contract-Level Chunking for Solidity Semantic Search

**Author:** AlexIT  
**Competition:** Data Forge — Week 4 (June 2026)

---

## Abstract

Semantic search has become a critical component of modern Retrieval-Augmented Generation (RAG) systems, especially for large codebases where traditional keyword search often fails to identify conceptually similar implementations.

This research explores how different chunking strategies affect retrieval quality for Solidity smart contracts and evaluates their practical suitability for Web3 development, smart contract auditing, and AI coding assistants.

The primary focus is understanding whether function-level chunking provides better semantic retrieval than contract-level indexing when working with real-world DeFi codebases.

---

## Background

Solidity code differs significantly from traditional application code.

Smart contracts often contain:

- Security-critical logic
- Reusable protocol patterns
- Access-control mechanisms
- NatSpec documentation
- Complex inheritance structures
- Financial calculations

Developers and auditors frequently search for behavior rather than exact text matches.

Typical examples include:

- Reentrancy protection
- Ownership verification
- Token transfer logic
- Flash-loan fee calculations
- Access-control implementations

These use cases make semantic retrieval particularly important.

---

## Chunking Strategies

### Contract-Level Chunking

In this approach, an entire Solidity contract is treated as a single document and embedded as one vector.

#### Advantages

- Maximum context preservation
- Simpler implementation
- Fewer indexed documents

#### Limitations

- Large contracts introduce significant noise
- Retrieval precision decreases
- Important functions become diluted inside larger contexts

For modern DeFi protocols, a single contract may contain dozens of unrelated logical components.

---

### Function-Level Chunking

Each function is indexed independently together with relevant metadata such as:

- Function signature
- NatSpec comments
- Modifiers
- Local context

#### Advantages

- Higher retrieval precision
- Better semantic granularity
- Smaller embedding payloads
- Improved relevance ranking

This strategy aligns closely with how developers and auditors reason about smart contract logic.

Example retrieval targets:

- `nonReentrant`
- `onlyOwner`
- `safeTransfer`
- Fee calculation functions
- Access-control checks

---

### Hybrid Chunking

Hybrid chunking combines function-level indexing with a limited amount of surrounding context.

Typical implementations include:

- Function body
- Nearby declarations
- Related state variables
- Contract metadata

This approach attempts to balance precision and contextual understanding.

---

## Embedding Models

### Voyage-code-3

Voyage-code-3 is designed specifically for source-code retrieval.

Potential strengths include:

- Strong code understanding
- Optimized semantic retrieval
- Better handling of programming constructs
- Suitability for code-focused RAG systems

Potential applications:

- Audit assistants
- Code search platforms
- AI development tools

---

### Jina Code Embeddings

Jina provides modern embedding models aimed at efficient semantic retrieval.

Potential strengths:

- Competitive retrieval quality
- Flexible deployment options
- Scalable indexing workflows

These models are increasingly used in production retrieval systems.

---

### OpenAI text-embedding-3-large

OpenAI's embedding model serves as a strong general-purpose baseline.

Potential strengths:

- Broad language understanding
- Mature ecosystem
- Reliable semantic representations

Potential limitation:

- Not specifically optimized for Solidity or source-code retrieval.

---

## Hybrid Search and Reranking

Pure vector search is often insufficient for production systems.

Important identifiers such as:

- Contract names
- Function names
- Error codes
- Protocol-specific terminology

may benefit from lexical retrieval.

A common production architecture combines:

1. BM25 retrieval
2. Vector similarity search
3. Reranking

This hybrid approach can improve both recall and ranking quality.

---

## Practical Applications

### Smart Contract Auditing

Auditors frequently need to locate similar implementations across multiple repositories.

Function-level retrieval can improve the discovery of relevant security patterns.

---

### AI Coding Assistants

Large language models require relevant context.

Semantic retrieval enables assistants to locate:

- Existing implementations
- Security mechanisms
- Protocol-specific patterns

before generating responses.

---

### Internal Developer Search

Protocol teams often maintain large codebases.

Semantic search can significantly reduce time spent locating relevant business logic.

---

### Vulnerability Research

Researchers can use retrieval systems to identify:

- Repeated security patterns
- Similar implementations
- Potential attack surfaces

across multiple projects.

---

## Expected Outcomes

Based on prior research in code retrieval and Retrieval-Augmented Generation systems, function-level chunking is expected to outperform contract-level chunking due to improved semantic granularity.

Hybrid retrieval approaches combining BM25 and vector search are also expected to improve ranking quality.

Code-specialized embedding models are expected to provide stronger retrieval performance than general-purpose embedding models when working with Solidity code.

---

## Limitations

This project represents an exploratory research effort rather than a full production benchmark.

Current limitations include:

- Small evaluation dataset
- Limited protocol coverage
- No large-scale benchmark execution
- Limited model comparison scope

Future work should expand both the dataset and evaluation methodology.

---

## Future Work

Potential future directions include:

- Larger Solidity datasets
- Additional DeFi protocols
- Reranking evaluation
- Vector database benchmarking
- Cost-performance analysis
- Long-context retrieval experiments

---

## Conclusion

Function-level chunking appears to be a promising strategy for Solidity semantic search because it closely matches the logical structure of smart contracts.

For production-grade Web3 retrieval systems, a combination of:

- Function-level chunking
- Hybrid retrieval
- Reranking
- Code-specialized embedding models

is expected to provide the strongest foundation for smart contract auditing, code discovery, and AI-assisted development workflows.

---

## Repository

GitHub Repository:

https://github.com/AlexITProf/solidity-semantic-search-evaluation

README:

https://github.com/AlexITProf/solidity-semantic-search-evaluation/blob/main/README.md
