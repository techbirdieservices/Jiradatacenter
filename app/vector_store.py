import numpy as np
import faiss
from embedding import get_embedding

def search_similar(index, stories, query, top_k=5):
    if index is None:
        raise ValueError("FAISS index not available")

    q_vector = np.array([get_embedding(query)], dtype='float32')
    distances, indices = index.search(q_vector, top_k)

    return [stories[i] for i in indices[0] if i < len(stories)]
