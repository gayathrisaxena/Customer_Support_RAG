from retrieval.bm25_search import BM25Retriever


class HybridRetriever:

    def __init__(self, vector_store, documents):
        self.vector_store = vector_store
        self.bm25 = BM25Retriever(documents)

    def search(self, query, top_k=3):

        # BM25 Search
        bm25_results = self.bm25.search(query, top_k)

        # Semantic Search (FAISS)
        semantic_results = self.vector_store.similarity_search(
            query,
            k=top_k
        )

        # Merge results and remove duplicates
        combined = []

        seen = set()

        for doc in bm25_results + semantic_results:

            if doc.page_content not in seen:
                seen.add(doc.page_content)
                combined.append(doc)

        return combined[:top_k]