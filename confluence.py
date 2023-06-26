from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import ConfluenceLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from colorama import Fore

from scripts.config import Config

cfg = Config()

loader = ConfluenceLoader(
    url=cfg.jira_site, username=cfg.jira_user, api_key=cfg.jira_api_key
)

# Setear la key del espacio de trabajo de confluence en space_key
# limit es la cantidad de documentos a cargar consulta que hará loader, no el total de documentos a traer.
docs = loader.load(space_key="EINV", include_attachments=False, limit=50,)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000, chunk_overlap=0, separators=[" ", ",", "\n"]
)

texts = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(texts, embeddings)

retriever = db.as_retriever()

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

while True:
    print(Fore.WHITE)
    query = input("> ")
    answer = qa.run(query)

    print(Fore.GREEN, answer)
