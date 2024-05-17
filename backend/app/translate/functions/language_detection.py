"""
This module contains the function to detect the language of the provided text.
"""
from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import SecretStr
from langchain_openai import ChatOpenAI

from app.settings import settings


def language_detection(text: str) -> str:
    """
    Detect the language of the given text.

    Args:
        text (str): Text to detect the language of.

    Returns:
        str: Detected language of the text.
    """
    client = ChatOpenAI(api_key=SecretStr(value=settings.OPENAI_API_KEY), model=settings.AI_MODEL)

    prompt_template = ChatPromptTemplate.from_template(template="""
        Detect the language of the provided passage. The language name should follow the BCP 47 standard.

        For example:
        - If the passage is "I'm learning how to translate texts with LLM models.", the output should be "en-US".
        - If the passage is "Estoy aprendiendo a traducir textos con modelos LLM.", the output should be "es-ES".
        - If the passage is "Estic aprenent a traduir textos amb models LLM.", the output should be "ca-ES".

        Passage:
        {text}
    """)

    customer_messages = prompt_template.format_messages(text=text)

    model_response = client.invoke(input=customer_messages)
    return model_response.content
