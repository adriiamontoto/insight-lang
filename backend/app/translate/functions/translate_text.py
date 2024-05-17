"""
This module contains the function to translate text to the specified language.
"""
from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import SecretStr
from langchain_openai import ChatOpenAI

from app.settings import settings


def translate_text(text: str, language: str) -> str:
    """
    Translate the text to the specified language.

    Args:
        text (str): Text to translate.
        language (str): Language to translate the text to as BCP 47 standard.

    Returns:
        str: Translated text.
    """
    client = ChatOpenAI(api_key=SecretStr(value=settings.OPENAI_API_KEY), model=settings.AI_MODEL)

    prompt_template = ChatPromptTemplate.from_template(template="""
        Translate the provided passage to {language}. The provided language follows the BCP 47 standard.

        For example:
        - If the passage is "I'm learning how to translate texts with LLM models." and the target language is "es-ES",
        the output should be "Estoy aprendiendo a traducir textos con modelos LLM.".
        - If the passage is "Estic aprenent a traduir textos amb models LLM." and the target language is "en-US",
        the output should be "I'm learning to translate texts with LLM models.".

        Passage:
        {text}
    """)
    model_response = client.invoke(input=prompt_template.format_messages(language=language, text=text))
    return model_response.content
