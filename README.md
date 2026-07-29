# 📞 Multi-Tenant Customer Support Ticket Assistant (Hybrid RAG)

An intelligent **Retrieval-Augmented Generation (RAG)** application that assists customer support teams by automatically retrieving relevant knowledge base articles, resolved tickets, and user manuals to generate accurate, context-aware support resolutions.

This project implements a **Hybrid Retrieval** architecture by combining **BM25 keyword search** and **FAISS semantic vector search**, powered by **LangChain**, **Groq Llama**, **Sentence Transformers**, and **Streamlit**.

---

# 🚀 Project Overview

Customer support teams often spend significant time searching through documentation, manuals, and previous tickets before responding to customer issues. This project automates that workflow using a Hybrid Retrieval-Augmented Generation (RAG) pipeline.

The application ingests support documents, removes sensitive customer information, performs document chunking, builds both keyword and semantic search indices, retrieves the most relevant information for a support ticket, and generates an AI-powered resolution using a Large Language Model.

---

# ✨ Features

- 📄 Upload Knowledge Base Articles (Markdown)
- 📑 Upload User Manuals (PDF)
- 📝 Upload Resolved Support Tickets (TXT)
- 🔒 Automatic PII Removal (Emails & Order IDs)
- ✂️ Intelligent Text Chunking
- 🔍 BM25 Keyword Retrieval
- 🧠 Semantic Search using Sentence Transformers
- ⚡ FAISS Vector Database
- 🔄 Hybrid Search (BM25 + FAISS)
- 🤖 AI-powered Customer Support Resolution using Groq Llama
- 🌐 Interactive Streamlit Web Interface

---

# 🏗️ Hybrid RAG Architecture

```
                Knowledge Base
                User Manuals
              Resolved Tickets
                      │
                      ▼
          Document Loading & Parsing
                      │
                      ▼
          Data Cleaning (PII Removal)
                      │
                      ▼
              Text Chunking
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
      BM25 Index          Sentence Embeddings
                                   │
                                   ▼
                          FAISS Vector Store
          └───────────┬────────────┘
                      ▼
               Hybrid Retrieval
            (BM25 + Semantic Search)
                      │
                      ▼
         Top Relevant Context Chunks
                      │
                      ▼
              Prompt Engineering
                      │
                      ▼
           Groq Llama Large Language Model
                      │
                      ▼
          AI-Generated Support Resolution
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| Framework | LangChain |
| Vector Database | FAISS |
| Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
| Keyword Search | BM25 |
| LLM | Groq Llama |
| Document Parsing | PyPDF, Markdown |
| Data Processing | Pandas, Regex |
| Environment | Python-dotenv |

---

# 📂 Project Structure

```
Customer_Support_RAG
│
├── data
│   ├── knowledge_base
│   ├── manuals
│   └── resolved_tickets
│
├── preprocessing
│   ├── ticket_loader.py
│   ├── cleaner.py
│   └── chunker.py
│
├── retrieval
│   ├── vector_store.py
│   ├── bm25_search.py
│   └── hybrid_search.py
│
├── llm
│   ├── prompt.py
│   └── rag_chain.py
│
├── utils
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/gayathrisaxena/Customer_Support_RAG.git
```

```bash
cd Customer_Support_RAG
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## Run the Application

```bash
python -m streamlit run app.py
```

---

# 📖 Workflow

1. Upload knowledge base articles, manuals, or resolved tickets.
2. Extract document content.
3. Remove sensitive customer information.
4. Split documents into semantic chunks.
5. Generate vector embeddings.
6. Store embeddings in a FAISS vector database.
7. Build a BM25 keyword index.
8. Perform Hybrid Retrieval using BM25 + FAISS.
9. Retrieve the top relevant context.
10. Generate a customer support resolution using Groq Llama.

---

# 💡 Sample Use Case

### Customer Ticket

> My printer is not turning on after installation.

### Retrieved Context

- Printer troubleshooting guide
- Previous resolved printer support ticket
- User manual instructions

### AI Resolution

The system retrieves the most relevant troubleshooting information and generates a clear, context-aware support response using the retrieved documents.

---

# 🎯 Key Highlights

- Hybrid Retrieval-Augmented Generation (RAG)
- Semantic Search using FAISS
- Keyword Search using BM25
- Prompt Engineering with LangChain
- Context-aware AI Response Generation
- Secure preprocessing with PII masking
- Modular and scalable architecture
- Industry-style customer support automation

---

# 🔮 Future Enhancements

- Multi-tenant support with isolated knowledge bases
- Conversation memory
- Role-based authentication
- Real-time ticket prioritization
- PostgreSQL document storage
- ElasticSearch integration
- Feedback-based response ranking
- Deployment using Docker and Kubernetes

---

# 👩‍💻 Author

**Gayathri Saxena**

MS in Artificial Intelligence
