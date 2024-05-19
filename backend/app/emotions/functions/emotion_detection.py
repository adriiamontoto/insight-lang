"""
This module contains the function to detect the emotion of the provided text.
"""
from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import SecretStr
from langchain_openai import ChatOpenAI

from app.settings import settings


def emotion_detection(text: str) -> str:
    """
    Detect the emotion of the given text.

    Args:
        text (str): Text to detect the emotion of.

    Returns:
        str: Detected emotion of the text.
    """
    client = ChatOpenAI(api_key=SecretStr(value=settings.OPENAI_API_KEY), model=settings.AI_MODEL)

    prompt_template = ChatPromptTemplate.from_template(template="""
        Detect the emotion of the provided passage. The passage can be with any language. The emotion name must be on
        lowercase and in english.

        For example:
        - If the passage is "The sun is shining, and the birds are singing.", the output should be "positive".
        - If the passage is "I cannot seem to find my keys anywhere.", the output should be "frustrated".
        - If the passage is "The movie ending was unexpected and left me speechless.", the output should be "surprised".
        - If the passage is "I miss the way things used to be.", the output should be "nostalgic".
        - If the passage is "My heart is pounding, and my palms are sweaty.", the output should be "anxious".
        - If the passage is "I cannot stop laughing at this joke.", the output should be "happy".

        Passage:
        {text}
    """)

    model_response = client.invoke(input=prompt_template.format_messages(text=text))
    return model_response.content
