from langchain.document_loaders import ConfluenceLoader
import pathlib
import sys
_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))
from scripts.vectordb import vectordb
from scripts.config import Config


cfg = Config()

loader = ConfluenceLoader(
    url=cfg.jira_site, username=cfg.jira_user, api_key=cfg.jira_api_key
)

docs = loader.load(
    space_key="VIF",
    include_attachments=False,
    limit=50,
)

_vectordb = vectordb("fondoscollection")
_vectordb.__init__("fondoscollection")
_vectordb.addFromDocuments(docs)
