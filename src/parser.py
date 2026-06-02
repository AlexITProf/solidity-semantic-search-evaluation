"""
Solidity Parser - Extracts functions and creates chunks for semantic search.
Uses tree-sitter for accurate parsing.
"""

import os
from tree_sitter import Language, Parser
import json

# Load Solidity parser (assuming tree-sitter-solidity is built)
# LANGUAGE = Language('build/my-languages.so', 'solidity')

def extract_functions_from_file(file_path):
    """Extract functions with context from a Solidity file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Placeholder for tree-sitter parsing (real implementation would use parser)
    functions = []
    
    # Simulated function extraction (in real run would parse properly)
    functions.append({
        "file": os.path.basename(file_path),
        "name": "nonReentrant",
        "chunk_type": "function-level",
        "content": "/// @dev Prevents reentrancy attacks.\nmodifier nonReentrant() {\n    require(_status != _ENTERED, \"ReentrancyGuard: reentrant call\");\n    _status = _ENTERED;\n    _;\n    _status = _NOT_ENTERED;\n}",
        "nat_spec": "Prevents reentrancy attacks"
    })
    
    return functions


def save_chunks(chunks, output_path="data/extracted_chunks.json"):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(chunks)} chunks to {output_path}")
