"""
similarity.py
-------------
Semantic similarity search for scientific papers using SBERT and FAISS.
"""

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


class PaperSimilarity:
    """Find semantically similar papers using SBERT embeddings and FAISS."""

    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.papers = []

    def build(self, papers: list, text_field: str = 'abstract') -> None:
        """
        Embed papers and build FAISS index.

        Args:
            papers: List of dicts with paper metadata
            text_field: Field to embed (default: 'abstract')
        """
        self.papers = papers
        texts = [p[text_field] for p in papers]
        embeddings = self.model.encode(texts).astype(np.float32)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def find_similar(self, query: str, top_k: int = 3) -> list:
        """
        Find most similar papers to a query.

        Args:
            query: Natural language query
            top_k: Number of results

        Returns:
            List of dicts with paper metadata and similarity score
        """
        if self.index is None:
            raise ValueError("Index not built. Call build() first.")

        query_embedding = self.model.encode([query]).astype(np.float32)
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            result = dict(self.papers[idx])
            result['similarity'] = float(1 / (1 + dist))
            results.append(result)

        return results