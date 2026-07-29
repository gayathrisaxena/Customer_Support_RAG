from preprocessing.ticket_loader import load_documents
from preprocessing.cleaner import clean_documents
from preprocessing.chunker import chunk_documents

docs = load_documents("data")
print(f"Documents Loaded: {len(docs)}")

cleaned_docs = clean_documents(docs)
print(f"Documents Cleaned: {len(cleaned_docs)}")

chunks = chunk_documents(cleaned_docs)
print(f"Chunks Created: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:300])