# Minimal wrapper using Chroma (local) via langchain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os


EMB_KEY = os.environ.get("OPENAI_API_KEY")
if not EMB_KEY:
raise Exception("OPENAI_API_KEY required for embeddings")


embeddings = OpenAIEmbeddings()


# Create or load a local Chroma store in ./db/chroma
def get_vectorstore(persist_directory: str = "./db/chroma"):
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
return vectordb


# Quick helper to upsert docs
def upsert_docs(texts: list[str], metadatas: list[dict] | None = None):
db = get_vectorstore()
db.add_texts(texts=texts, metadatas=metadatas)
