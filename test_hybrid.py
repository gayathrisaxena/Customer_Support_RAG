from preprocessing.ticket_loader import load_documents
from preprocessing.cleaner import clean_documents
from preprocessing.chunker import chunk_documents

from retrieval.vector_store import create_vector_store
from retrieval.hybrid_search import HybridRetriever

# Load documents
docs = load_documents("data")

# Clean
docs = clean_documents(docs)

# Chunk
chunks = chunk_documents(docs)

# Create FAISS
vector_store = create_vector_store(chunks)

# Hybrid Retriever
retriever = HybridRetriever(
    vector_store,
    chunks
)

# Query
results = retriever.search(
    "printer not working",
    top_k=3
)

print(f"\nRetrieved {len(results)} document(s)\n")

for i, doc in enumerate(results, start=1):
    print("=" * 60)
    print(f"Document {i}")
    print("=" * 60)
    print(doc.page_content)