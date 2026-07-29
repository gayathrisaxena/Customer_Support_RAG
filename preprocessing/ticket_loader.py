from pathlib import Path
from langchain_core.documents import Document
from pypdf import PdfReader
from bs4 import BeautifulSoup
import markdown


def load_pdf(file_path):
    """Load text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def load_markdown(file_path):
    """Load text from a Markdown (.md) file."""
    with open(file_path, "r", encoding="utf-8") as f:
        md = f.read()

    html = markdown.markdown(md)
    text = BeautifulSoup(html, "html.parser").get_text()

    return text


def load_text(file_path):
    """Load text from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_documents(data_folder):
    """
    Load all supported documents from a folder.
    Supports: PDF, Markdown, TXT
    """

    documents = []

    for file in Path(data_folder).rglob("*"):

        suffix = file.suffix.lower()

        if suffix == ".pdf":
            text = load_pdf(file)

        elif suffix == ".md":
            text = load_markdown(file)

        elif suffix == ".txt":
            text = load_text(file)

        else:
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": str(file),
                    "file_name": file.name,
                    "file_type": suffix
                }
            )
        )

    return documents


if __name__ == "__main__":

    docs = load_documents("data")

    print(f"\nLoaded {len(docs)} documents\n")

    for doc in docs:
        print(doc.metadata)