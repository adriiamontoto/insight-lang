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
        language (str): Language to translate the text to.

    Returns:
        str: Translated text.
    """
    client = ChatOpenAI(api_key=SecretStr(value=settings.OPENAI_API_KEY), model='gpt-3.5-turbo')

    prompt_template = ChatPromptTemplate.from_template(
        template='Translate the text that is delimited by triple backticks to {language}. text: ```{text}```')

    customer_messages = prompt_template.format_messages(language=language, text=text)

    model_response = client.invoke(input=customer_messages)
    return model_response.content
