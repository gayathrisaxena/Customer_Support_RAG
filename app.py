import streamlit as st
import tempfile
import shutil
from pathlib import Path

from preprocessing.ticket_loader import load_documents
from preprocessing.cleaner import clean_documents
from preprocessing.chunker import chunk_documents

from retrieval.vector_store import create_vector_store
from retrieval.hybrid_search import HybridRetriever

from llm.rag_chain import generate_response

st.set_page_config(page_title="Customer Support RAG", layout="wide")

st.title("📞 Multi-Tenant Customer Support Ticket Assistant")

st.write(
    "Upload your knowledge base, manuals, or resolved tickets and ask a customer support question."
)

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf", "txt", "md"],
    accept_multiple_files=True
)

question = st.text_area("Customer Ticket")

if st.button("Generate Resolution"):

    if not uploaded_files:
        st.warning("Please upload at least one document.")
        st.stop()

    if not question.strip():
        st.warning("Please enter a customer ticket.")
        st.stop()

    with tempfile.TemporaryDirectory() as temp_dir:

        for file in uploaded_files:
            file_path = Path(temp_dir) / file.name

            with open(file_path, "wb") as f:
                shutil.copyfileobj(file, f)

        docs = load_documents(temp_dir)

        docs = clean_documents(docs)

        chunks = chunk_documents(docs)

        vector_store = create_vector_store(chunks)

        retriever = HybridRetriever(
            vector_store,
            chunks
        )

        retrieved_docs = retriever.search(
            question,
            top_k=3
        )

        answer = generate_response(
            question,
            retrieved_docs
        )

        st.subheader("Retrieved Documents")

        for i, doc in enumerate(retrieved_docs, start=1):
            st.markdown(f"### Document {i}")
            st.write(doc.page_content)

        st.subheader("AI Resolution")

        st.success(answer)