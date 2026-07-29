from preprocessing.ticket_loader import load_documents
from preprocessing.cleaner import clean_documents
from preprocessing.chunker import chunk_documents

from retrieval.bm25_search import BM25Retriever

docs = load_documents("data")
docs = clean_documents(docs)
chunks = chunk_documents(docs)

bm25 = BM25Retriever(chunks)

results = bm25.search(
    "printer not working",
    top_k=3
)

print(f"Retrieved {len(results)} documents\n")

for doc in results:
    print(doc.page_content)
    print("-" * 50)