"""Text embedding helpers for the chatbot RAG pipeline.

This implementation is dependency-light and deterministic so it can run in the
current project without extra setup. The vectors can later be swapped with a
Chroma/transformers embedding backend if needed.
"""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter
from typing import Iterable, List

_TOKEN_PATTERN = re.compile(r"[a-z0-9']+")


def tokenize(text: str) -> list[str]:
    """Convert raw text into normalized tokens."""

    return _TOKEN_PATTERN.findall(text.lower())


def _hash_token(token: str, dimensions: int) -> int:
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") % dimensions


def embed_text(text: str, dimensions: int = 384) -> list[float]:
    """Turn a piece of text into a fixed-size numeric vector."""

    vector = [0.0] * dimensions
    tokens = tokenize(text)

    if not tokens:
        return vector

    counts = Counter(tokens)
    total = float(len(tokens))

    for token, count in counts.items():
        index = _hash_token(token, dimensions)
        vector[index] += count / total

    norm = math.sqrt(sum(value * value for value in vector))
    if norm:
        vector = [value / norm for value in vector]

    return vector


def embed_texts(texts: Iterable[str], dimensions: int = 384) -> List[list[float]]:
    """Embed multiple texts in one call."""

    return [embed_text(text, dimensions=dimensions) for text in texts]
