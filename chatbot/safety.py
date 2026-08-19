_BLOCKED_PATTERNS = (
    "suicide",
    "self-harm",
    "self harm",
    "kill myself",
    "overdose",
    "dosage",
    "prescription",
    "medicine dose",
    "how much ibuprofen",
    "how much paracetamol",
    "antibiotic",
)

_SAFETY_REDIRECT_MESSAGE = (
    "I'm not able to help with medication dosages, prescriptions, or urgent health "
    "and safety concerns. Please contact a doctor, pharmacist, or local emergency "
    "services for anything in that category — they can give you accurate, "
    "personalized advice."
)


def contains_blocked_content(user_message: str) -> bool:
    lowered = user_message.lower()
    return any(pattern in lowered for pattern in _BLOCKED_PATTERNS)


def get_safety_redirect_message() -> str:
    return _SAFETY_REDIRECT_MESSAGE


def build_safety_prompt(user_message: str, condition: str = "", kb_info: str = "") -> str:
    context_block = ""
    if condition:
        context_block += (
            f"\nThe user's most recent screening result was: {condition}. "
            f"This is just background context — the user is free to ask about "
            f"this condition, general skin health, or any other skin concern."
        )
    else:
        context_block += (
            "\nNo specific screening result is available in this conversation. "
            "If the user asks what their result was or what condition was "
            "predicted, tell them clearly that you don't have that information "
            "here and they should check their result on the DermaScan results "
            "page — do NOT guess or name a specific condition."
        )
    if kb_info:
        context_block += f"\n\nReference guidance for their recent result:\n{kb_info}"

    prompt = f"""You are a helpful assistant for DermaScan, a skin disease screening app.

Rules you must always follow:
- You can answer general questions about ANY skin condition, not just the user's most recent result.
- NEVER state or guess a specific diagnosis or predicted condition unless it is explicitly given to you in the context below.
- Never give a definitive medical diagnosis.
- Never provide medication dosages, prescriptions, or drug-combination advice.
- If reference guidance is provided below and it matches the topic being asked about, use it. Otherwise, answer from your general knowledge of dermatology.
- Always encourage the user to consult a certified dermatologist for serious or worsening symptoms.
- Keep answers clear, simple, and concise (2-4 sentences).
- Only redirect the conversation if the question has NOTHING to do with skin, health, or the app itself (e.g. politics, sports, unrelated topics).
{context_block}

User's question: {user_message}"""

    return prompt