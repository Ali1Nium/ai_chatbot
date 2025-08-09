import json
import logging
from django.conf import settings
from openai import AsyncOpenAI
from typing import List, Dict, Optional, Any

logger = logging.getLogger(__name__)

OPENAI_API_KEY = settings.OPENAI_API_KEY
MAX_TOKENS = 1500

async def call_llm(
    model_name: str = "gpt-4o-mini",
    model_temp: float = 0.7,
    messages: List[Dict[str, str]] = None,
    response_format: Optional[Any] = None,
) -> Any:

    if not messages:
        messages = [{
            "role": "system",
            "content": "We apologize, but the return service is temporarily unavailable. Please try again later."
        }]

    logger.info(f"[call_llm] Model: {model_name} | Temp: {model_temp}")

    client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    try:
        if response_format:
            logger.info("[call_llm] Response format is provided")
            completion = await client.beta.chat.completions.parse(
                model=model_name,
                messages=messages,
                response_format=response_format,
                temperature=model_temp,
                max_tokens=MAX_TOKENS,
            )
        else:
            logger.info("[call_llm] No response format provided")
            completion = await client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=model_temp,
                max_tokens=MAX_TOKENS,
            )

        logger.info("[call_llm] Success")
        return completion.choices[0].message.content

    except Exception as e:
        logger.error(f"[call_llm] Error: {str(e)}", exc_info=True)
        return None
