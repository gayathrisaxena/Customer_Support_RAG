from preprocessing.ticket_loader import load_documents
from preprocessing.cleaner import clean_documents
from preprocessing.chunker import chunk_documents

from retrieval.vector_store import create_vector_store
from retrieval.hybrid_search import HybridRetriever

from llm.rag_chain import generate_response


# Load documents
docs = load_documents("data")

# Clean
docs = clean_documents(docs)

# Chunk
chunks = chunk_documents(docs)

# Create vector store
vector_store = create_vector_store(chunks)

# Hybrid Search
retriever = HybridRetriever(
    vector_store,
    chunks
)

question = "My printer is not turning on."

retrieved_docs = retriever.search(
    question,
    top_k=3
)

response = generate_response(
    question,
    retrieved_docs
)

print("\nCustomer Question:\n")
print(question)

print("\nRetrieved Documents:", len(retrieved_docs))

print("\nAI Response:\n")
print(response)