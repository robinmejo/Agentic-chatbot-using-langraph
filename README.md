# 🤖 Agentic Chatbot using LangGraph

An AI-powered agentic chatbot built using **Python, LangChain, LangGraph, and Streamlit**.

The application supports tool calling, conversational memory, RAG-based document search, and multiple external tools such as web search, weather, and stock price lookup.

---

## 🚀 Features

- 💬 Conversational AI chatbot
- 🧠 LangGraph-based agent workflow
- 🔧 LLM tool calling
- 📄 PDF document upload
- 🔍 RAG-based document search
- 🗃️ Chroma vector database
- 💾 SQLite-based conversation/checkpoint persistence
- 🌐 Web search using Tavily
- 🌤️ Weather information
- 📈 Stock price lookup
- 🧮 Calculator tool
- 🎨 Streamlit user interface
- 🔐 Environment variable based API key management

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │   Streamlit UI  │
                    │     app.py      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    LangGraph    │
                    │   Agent Graph   │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       ┌─────────────┐               ┌─────────────┐
       │     LLM     │               │    Tools    │
       │  OpenAI     │               │ Calculator  │
       └─────────────┘               │ Web Search  │
                                     │ Weather     │
                                     │ Stock       │
                                     │ Document RAG│
                                     └──────┬──────┘
                                            │
                                            ▼
                                    ┌──────────────┐
                                    │    Chroma    │
                                    │ Vector Store │
                                    └──────────────┘