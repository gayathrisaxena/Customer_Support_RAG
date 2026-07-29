from preprocessing.ticket_loader import load_documents
from preprocessing.cleaner import clean_documents
from preprocessing.chunker import chunk_documents
from retrieval.vector_store import create_vector_store

docs = load_documents("data")
docs = clean_documents(docs)
chunks = chunk_documents(docs)

vector_store = create_vector_store(chunks)

print("Vector Store Created Successfully!")