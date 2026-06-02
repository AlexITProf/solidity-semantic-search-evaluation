"""
Evaluation script - Calculates retrieval metrics.
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_recall_at_k(retrieved, relevant, k=5):
    """Calculate Recall@K"""
    retrieved_k = retrieved[:k]
    return len(set(retrieved_k) & set(relevant)) / len(relevant)

def calculate_mrr(retrieved, relevant):
    """Calculate Mean Reciprocal Rank"""
    for i, item in enumerate(retrieved):
        if item in relevant:
            return 1 / (i + 1)
    return 0

def evaluate_model(results_df):
    """Evaluate model performance"""
    metrics = {
        "Recall@5": results_df["recall_5"].mean(),
        "MRR": results_df["mrr"].mean(),
        "NDCG@10": results_df["ndcg_10"].mean()
    }
    return metrics

if __name__ == "__main__":
    # Load results
    df = pd.read_csv("data/results_summary.csv")
    print(evaluate_model(df))
