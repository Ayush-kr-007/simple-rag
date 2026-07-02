import numpy as np


def chunk_text(
        text,
        chunk_size=500,
        overlap=50
):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += chunk_size - overlap

    return chunks


def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )


def retrieve(
        query,
        chunks,
        embeddings,
        model,
        top_k=3
):
    query_embedding = model.encode(
        query,
        convert_to_numpy=True
    )

    similarities = []

    for emb in embeddings:
        score = cosine_similarity(
            query_embedding,
            emb
        )

        similarities.append(score)

    similarities = np.array(similarities)

    top_indices = similarities.argsort()[-top_k:][::-1]

    retrieved_chunks = [
        chunks[i]
        for i in top_indices
    ]

    return retrieved_chunks