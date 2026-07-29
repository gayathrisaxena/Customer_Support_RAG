from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME
from llm.prompt import PROMPT_TEMPLATE


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)


def generate_response(question, retrieved_docs):
    """
    Generate a response using the retrieved documents.
    """

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = PROMPT_TEMPLATE.format(
        question=question,
        context=context
    )

    response = llm.invoke(prompt)

    return response.content