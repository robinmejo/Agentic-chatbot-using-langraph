from pathlib import Path

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


# ------------------------------------------------------------
# Storage path
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

CHROMA_DIR = BASE_DIR / "chroma_db"


# ------------------------------------------------------------
# Chroma collection
# ------------------------------------------------------------

COLLECTION_NAME = "agent_documents"


# ------------------------------------------------------------
# Embeddings
# ------------------------------------------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# ------------------------------------------------------------
# Vector store
# ------------------------------------------------------------

def get_vector_store():

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(
            CHROMA_DIR
        ),
    )

    return vector_store