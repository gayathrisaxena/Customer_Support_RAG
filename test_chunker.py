from preprocessing.ticket_loader import load_documents
from preprocessing.cleaner import clean_documents
from preprocessing.chunker import chunk_documents

docs = load_documents("data")
print("Loaded Documents:", len(docs))

for doc in docs:
    print(doc.metadata)

docs = clean_documents(docs)

chunks = chunk_documents(docs)

print("Created Chunks:", len(chunks))

if chunks:
    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)
else:
    print("No chunks were created.")