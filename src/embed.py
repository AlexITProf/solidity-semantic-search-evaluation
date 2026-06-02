"""
Embedding generation using Voyage, Jina, and OpenAI models.
"""

from voyageai import Client as VoyageClient
from openai import OpenAI
from jina import Client as JinaClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_voyage_embeddings(texts):
    """Get embeddings using Voyage-code-3"""
    vo = VoyageClient(api_key=os.getenv("VOYAGE_API_KEY"))
    result = vo.embed(texts=texts, model="voyage-code-3", input_type="document")
    return result.embeddings

def get_openai_embeddings(texts):
    """Get embeddings using OpenAI text-embedding-3-large"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-large"
    )
    return [data.embedding for data in response.data]

def get_jina_embeddings(texts):
    """Get embeddings using Jina Code model"""
    client = JinaClient(token=os.getenv("JINA_API_KEY"))
    # Example call - adjust according to actual Jina API
    result = client.embeddings.create(
        input=texts,
        model="jina-embeddings-v3"
    )
    return result.embeddings

# Example usage
if __name__ == "__main__":
    sample_texts = ["Implementation of ReentrancyGuard", "Calculate flash loan fee"]
    embeddings = get_voyage_embeddings(sample_texts)
    print(f"Generated {len(embeddings)} embeddings")
