import abc
import chromadb
import uuid
from chromadb.config import Settings
from scripts.config import Config
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


class Singleton(abc.ABCMeta, type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method for the singleton metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AbstractSingleton(abc.ABC, metaclass=Singleton):
    pass


cfg = Config()


class vectordb(metaclass=Singleton):
    __client = None
    __collection_name = None

    ### Inicializa la base de datos de vectores
    def __init__(self, _collection) -> None:
        self.__collection_name = _collection
        
        self.__client = Chroma(
            collection_name=self.__collection_name,
            embedding_function=self.get_embeddings(),
            client_settings=Settings(
                chroma_api_impl="rest",
                chroma_server_host=cfg.chroma_server_host,
                chroma_server_http_port=cfg.chroma_server_port,
            ),
        )

    def addDocumentsWithMetadata(self, docs):
        Chroma(client=self.__client, collection_name=self.__collection_name)
        collection = self.__client.get_collection(self.__collection_name)

        for doc in docs:
            collection.add(
                ids=[str(uuid.uuid1())],
                metadatas=doc.metadata,
                documents=doc.page_content,
                embeddings=self.get_embeddings(),
            )

    def addFromDocuments(self, _docs):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=4000,
            chunk_overlap=0,
            separators=["", " ", "\n", "\n\n", "(?<=\. )"],
        )

        texts = text_splitter.split_documents(_docs)

        Chroma.from_documents(
            documents=texts,
            embedding=self.get_embeddings(),
            collection_name=self.__collection_name,
        )

    def searchDocument(self, query, _k=2):
        # tell LangChain to use our client and collection name
        collection = self.__client.get_collection(self.__collection_name)
        docs = collection.similarity_search(query, k=_k)
        return docs[0].page_content

    def get_collection(self):
        return self.__collection_name

    def get_embeddings(self):
        embeddings = OpenAIEmbeddings()
        return embeddings

    def get_as_retriever(self):      
        vectordb = Chroma(client=self.__client, collection_name=self.__collection_name)
        
        return vectordb.as_retriever()

    # def updateDeleteDocument():
    #     # create simple ids
    #     ids = [str(i) for i in range(1, len(docs) + 1)]

    #     # add data
    #     example_db = Chroma.from_documents(docs, embedding_function, ids=ids)
    #     docs = example_db.similarity_search(query)
    #     print(docs[0].metadata)

    #     # update the metadata for a document
    #     docs[0].metadata = {
    #         "source": "../../../state_of_the_union.txt",
    #         "new_value": "hello world",
    #     }
    #     example_db.update_document(ids[0], docs[0])
    #     print(example_db._collection.get(ids=[ids[0]]))

    #     # delete the last document
    #     print("count before", example_db._collection.count())
    #     example_db._collection.delete(ids=[ids[-1]])
    #     print("count after", example_db._collection.count())
