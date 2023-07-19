# Ejemplo de uso de un prompt que se conecta a Confluence y genera casos de prueba del requerimiento que se le asigne

from langchain.document_loaders import ConfluenceLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

from langchain.vectorstores import Chroma
from colorama import Fore

import pathlib
import sys

_parentdir = pathlib.Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, str(_parentdir))
print(_parentdir)

from scripts.config import Config

cfg = Config()

loader = ConfluenceLoader(
    url=cfg.jira_site, username=cfg.jira_user, api_key=cfg.jira_api_key
)

# Setear la key del espacio de trabajo de confluence en space_key
# limit es la cantidad de documentos a cargar consulta que hará loader, no el total de documentos a traer.
docs = loader.load(
    space_key="VIF",
    include_attachments=False,
    limit=50,
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000, chunk_overlap=0, separators=["", " ", "\n", "\n\n", "(?<=\. )"]
)
persist_directory = "examples/docs/chroma"

texts = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=texts, embedding=embeddings, persist_directory=persist_directory
)

question = "como esco fondos resuelve la funcionalidad de alquiler de títulos"
docs = vectordb.similarity_search(question, k=5)

vectordb.persist()

for doc in docs:
    print(doc.metadata)

print(docs[0].page_content)

