# Script para simplificar la info a ingestar en la base de datos de vectores usando multiples loaders

import os
import pathlib
import sys
import chromadb
from langchain.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    ConfluenceLoader,
)
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))
from scripts.vectordb import vectordb
from scripts.config import Config

cfg = Config()


ABS_PATH: str = os.path.dirname(os.path.abspath(__file__))
DB_DIR: str = os.path.join(ABS_PATH, "db")


# Create vector database
def create_vector_database():
    """
    Creates a vector database using document loaders and embeddings.

    This function loads data from PDF, markdown and text files in the 'data/' directory,
    splits the loaded documents into chunks, transforms them into embeddings using HuggingFace,
    and finally persists the embeddings into a Chroma vector database.

    """
    # Initialize loaders for different file types
    pdf_loader = DirectoryLoader("data/", glob="**/*.pdf", loader_cls=PyPDFLoader)

    # confluence_loader = ConfluenceLoader(
    #     url=cfg.jira_site, username=cfg.jira_user, api_key=cfg.jira_api_key
    # )

    # confluence_loader = confluence_loader.load(
    #     space_key="VIF",
    #     include_attachments=False,
    #     limit=50,
    # )

    all_loaders = [pdf_loader]

    # Load documents from all loaders
    loaded_documents = []
    for loader in all_loaders:
        loaded_documents.extend(loader.load())

    # Split loaded documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150, separators=["", " ", "\n", "\n\n", "(?<=\. )"])
    chunked_documents = text_splitter.split_documents(loaded_documents)

    # Initialize HuggingFace embeddings
    huggingface_embeddings = HuggingFaceInstructEmbeddings(
        model_name="hkunlp/instructor-xl", model_kwargs={"device": "cpu"}
    )

    client = chromadb.HttpClient(
        host=cfg.chroma_server_host, port=cfg.chroma_server_port,
    )

    Chroma.from_documents(
        client=client,
        documents=chunked_documents[0:512],
        embedding=huggingface_embeddings,
        collection_name="fondoscollection",
    )

    # Create and persist a Chroma vector database from the chunked documents
    # vector_database = Chroma.from_documents(
    #     documents=chunked_documents,
    #     embedding=huggingface_embeddings,
    # )

    # _vectordb = vectordb("fondoscollection")
    # _vectordb.__init__("fondoscollection")
    # _vectordb.addChunkedDocuments(chunked_documents, huggingface_embeddings)

    # vector_database.persist()


if __name__ == "__main__":
    create_vector_database()
