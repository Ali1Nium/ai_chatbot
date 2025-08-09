from typing import List, Dict, Optional


async def build_llm_messages(
    prompt_system: str,
    user_input: str,
    file_context: Optional[str] = None,
    web_context: Optional[str] = None,
    chat_history: Optional[List[Dict[str, str]]] = None,
) -> List[Dict[str, str]]:

    messages: List[Dict[str, str]] = []

    if prompt_system:
        messages.append({"role": "system", "content": prompt_system})

    if chat_history:
        for msg in chat_history:
            messages.append({"role": msg["role"], "content": msg["content"]})

    if file_context:
        messages.append({"role": "system", "content": f"[File Info]\n{file_context}"})

    if web_context:
        messages.append({"role": "system", "content": f"[Web Search]\n{web_context}"})

    if user_input:
        messages.append({"role": "user", "content": user_input})

    return messages
