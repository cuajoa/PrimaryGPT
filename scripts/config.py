import os
import openai
from dotenv import load_dotenv
import abc

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

# Load environment variables from .env file
load_dotenv()

class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self):
        """Initialize the Config class"""
        self.debug_mode = False

        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        # Initialize the OpenAI API client
        openai.api_key = self.openai_api_key

        self.jira_user = os.getenv("JIRA_USER")
        self.jira_api_key = os.getenv("JIRA_API_KEY")
        self.jira_site = os.getenv("JIRA_SITE")
        self.chroma_server_host = os.getenv("CHROMA_SERVER_HOST")
        self.chroma_server_port = os.getenv("CHROMA_SERVER_PORT")

    def set_openai_api_key(self, value: str):
        """Set the OpenAI API key value."""
        self.openai_api_key = value

    def set_jira_user(self, value: str):
        """Set the JIRA USER value."""
        self.jira_user = value

    def set_jira_api_key(self, value: str):
        """Set the JIRA API KEY value."""
        self.jira_api_key = value

    def set_jira_site(self, value: str):
        """Set the JIRA site value."""
        self.jira_site = value

    def set_chroma_server_host(self, value: str):
        """Set the chroma host value."""
        self.chroma_server_host = value

    def set_chroma_server_port(self, value: str):
        """Set the chroma port value."""
        self.chroma_server_port = value

    def set_debug_mode(self, value: bool):
        """Set the debug mode value."""
        self.debug_mode = value
