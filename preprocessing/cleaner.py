import re
from langchain_core.documents import Document


def clean_text(text):
    """
    Remove sensitive customer information.
    """

    # Remove email addresses
    text = re.sub(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "[EMAIL]",
        text,
    )

    # Remove order IDs like ORD12345 or ORDER-56789
    text = re.sub(
        r"\b(?:ORD|ORDER)[-_]?\d+\b",
        "[ORDER_ID]",
        text,
        flags=re.IGNORECASE,
    )

    return text


def clean_documents(documents):
    """
    Clean all loaded documents.
    """

    cleaned_docs = []

    for doc in documents:
        cleaned_docs.append(
            Document(
                page_content=clean_text(doc.page_content),
                metadata=doc.metadata
            )
        )

    return cleaned_docs