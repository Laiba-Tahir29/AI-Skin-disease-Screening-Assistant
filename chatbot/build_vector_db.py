import os
import json
import faiss
import numpy as np

from chatbot.embeddings import embed_text


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_DIR = os.path.join(BASE_DIR, "knowledge_base")
VECTOR_DIR = os.path.join(BASE_DIR, "vector_db")

DIMENSIONS = 384
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100


def chunk_text(text: str):
    chunks = []

    start = 0
    step = CHUNK_SIZE - CHUNK_OVERLAP

    while start < len(text):
        chunk = text[start:start + CHUNK_SIZE].strip()

        if chunk:
            chunks.append(chunk)

        start += step

    return chunks


def build_vector_database():

    os.makedirs(VECTOR_DIR, exist_ok=True)

    documents = []

    for filename in os.listdir(KB_DIR):

        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(KB_DIR, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        chunks = chunk_text(text)

        for chunk in chunks:
            documents.append({
                "text": chunk,
                "source": filename
            })

    print(f"Loaded {len(documents)} knowledge chunks.")

    if not documents:
        print("No .txt files found in knowledge_base.")
        return

    vectors = [
        embed_text(doc["text"], dimensions=DIMENSIONS)
        for doc in documents
    ]

    vectors = np.array(vectors, dtype="float32")

    index = faiss.IndexFlatIP(DIMENSIONS)
    index.add(vectors)

    index_path = os.path.join(
        VECTOR_DIR,
        "knowledge_base.index"
    )

    documents_path = os.path.join(
        VECTOR_DIR,
        "documents.json"
    )

    faiss.write_index(index, index_path)

    with open(documents_path, "w", encoding="utf-8") as file:
        json.dump(
            documents,
            file,
            ensure_ascii=False,
            indent=2
        )

    print("Vector database created successfully!")
    print(f"Index: {index_path}")
    print(f"Documents: {documents_path}")
    print(f"Total chunks: {len(documents)}")


if __name__ == "__main__":
    build_vector_database()