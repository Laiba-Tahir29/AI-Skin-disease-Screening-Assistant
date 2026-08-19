import os
import json
import time
import faiss
import numpy as np

from dotenv import load_dotenv
from google import genai

from chatbot.embeddings import embed_text
from chatbot.safety import (
    build_safety_prompt,
    contains_blocked_content,
    get_safety_redirect_message,
)

# ============================================================
# LOAD .ENV
# ============================================================

load_dotenv()


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTOR_DIR = os.path.join(
    BASE_DIR,
    "vector_db"
)

INDEX_PATH = os.path.join(
    VECTOR_DIR,
    "knowledge_base.index"
)

DOCUMENTS_PATH = os.path.join(
    VECTOR_DIR,
    "documents.json"
)


# ============================================================
# RAG SETTINGS
# ============================================================

DIMENSIONS = 384
TOP_K = 3


# ============================================================
# GEMINI CLIENT
# ============================================================

_client = None


def get_client():
    """
    Create the Gemini client using GEMINI_API_KEY
    from the .env file.
    """

    global _client

    if _client is None:

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. "
                "Check your .env file."
            )

        _client = genai.Client(
            api_key=api_key
        )

    return _client


# ============================================================
# LOAD FAISS VECTOR DATABASE
# ============================================================

def load_vector_database():
    """
    Load the FAISS index and the original
    knowledge chunks.
    """

    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError(
            f"Vector database not found:\n{INDEX_PATH}"
        )

    if not os.path.exists(DOCUMENTS_PATH):
        raise FileNotFoundError(
            f"Documents file not found:\n{DOCUMENTS_PATH}"
        )

    # Load FAISS index
    index = faiss.read_index(
        INDEX_PATH
    )

    # Load original text chunks
    with open(
        DOCUMENTS_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        documents = json.load(file)

    return index, documents


# ============================================================
# RETRIEVAL
# ============================================================

def retrieve_relevant_information(
    user_message: str,
    top_k: int = TOP_K
) -> str:
    """
    Convert the user's question into an embedding,
    search FAISS for similar vectors,
    and return the most relevant knowledge chunks.
    """

    start_time = time.time()

    # Load vector database
    index, documents = load_vector_database()

    print(
        f"[RAG] Vector database loaded in "
        f"{time.time() - start_time:.3f}s"
    )

    # --------------------------------------------------------
    # Convert user question into embedding
    # --------------------------------------------------------

    query_vector = embed_text(
        user_message,
        dimensions=DIMENSIONS
    )

    query_vector = np.array(
        [query_vector],
        dtype="float32"
    )

    print(
        f"[RAG] Query embedding created in "
        f"{time.time() - start_time:.3f}s"
    )

    # --------------------------------------------------------
    # Search FAISS
    # --------------------------------------------------------

    scores, indices = index.search(
        query_vector,
        top_k
    )

    print(
        f"[RAG] FAISS search completed in "
        f"{time.time() - start_time:.3f}s"
    )

    retrieved_chunks = []

    # --------------------------------------------------------
    # Get original documents
    # --------------------------------------------------------

    for position, index_number in enumerate(indices[0]):

        if index_number == -1:
            continue

        if index_number >= len(documents):
            continue

        document = documents[index_number]

        score = float(
            scores[0][position]
        )

        print(
            f"[RAG] Result {position + 1}: "
            f"{document.get('source', 'unknown')} "
            f"(score: {score:.4f})"
        )

        retrieved_chunks.append(
            f"Source: {document.get('source', 'Unknown')}\n"
            f"{document.get('text', '')}"
        )

    return "\n\n---\n\n".join(
        retrieved_chunks
    )


# ============================================================
# MAIN CHATBOT FUNCTION
# ============================================================

def get_chatbot_response(
    user_message: str,
    condition: str = ""
) -> str:
    """
    Complete RAG pipeline:

    1. Safety check
    2. Convert question to embedding
    3. Retrieve relevant chunks using FAISS
    4. Build safety-aware prompt
    5. Send prompt to Gemini
    6. Return Gemini response
    """

    total_start = time.time()

    print("\n================ CHATBOT REQUEST ================")
    print(f"[CHAT] User: {user_message}")

    # ========================================================
    # 1. SAFETY CHECK
    # ========================================================

    if contains_blocked_content(
        user_message
    ):

        print(
            "[CHAT] Blocked by safety layer."
        )

        return get_safety_redirect_message()

    print(
        f"[CHAT] Safety check: "
        f"{time.time() - total_start:.3f}s"
    )

    # ========================================================
    # 2. RETRIEVE KNOWLEDGE FROM FAISS
    # ========================================================

    kb_info = retrieve_relevant_information(
        user_message,
        top_k=TOP_K
    )

    print(
        f"[CHAT] Retrieval complete: "
        f"{time.time() - total_start:.3f}s"
    )

    # ========================================================
    # 3. BUILD PROMPT
    # ========================================================

    prompt = build_safety_prompt(
        user_message,
        condition,
        kb_info
    )

    print(
        f"[CHAT] Prompt built: "
        f"{time.time() - total_start:.3f}s"
    )

    # ========================================================
    # 4. CALL GEMINI
    # ========================================================

    client = get_client()

    print(
        "[CHAT] Calling Gemini..."
    )

    gemini_start = time.time()

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    print(
        f"[CHAT] Gemini response received in "
        f"{time.time() - gemini_start:.3f}s"
    )

    # ========================================================
    # 5. RETURN RESPONSE
    # ========================================================

    print(
        f"[CHAT] TOTAL TIME: "
        f"{time.time() - total_start:.3f}s"
    )

    print(
        "=================================================\n"
    )

    return response.text