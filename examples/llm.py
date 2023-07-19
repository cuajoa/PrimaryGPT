from colorama import Fore, Style
from scripts.config import Config
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chains import LLMChain
from langchain.prompts import prompt

cfg = Config()


def check_openai_api_key():
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    if not cfg.openai_api_key:
        print(
            Fore.RED
            + "Please set your OpenAI API key in config.py or as an environment variable."
        )
        print("You can get your key from https://beta.openai.com/account/api-keys")
        exit(1)


check_openai_api_key()
cfg = Config()

llm = OpenAI(openai_api_key=cfg.openai_api_key, temperature=0.9)

llm.predict(
    "What would be a good company name for a company that makes colorful socks?"
)
# chat = ChatOpenAI(temperature=0)
# chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming.")])


# chain = LLMChain(llm=llm, prompt=prompt)
# chain.run("colorful socks")
