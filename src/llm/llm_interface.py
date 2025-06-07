import logging
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
logging.basicConfig(level=logging.INFO,format='%(levelname)s:%(message)s')
logging.info("starting the tool calling process")
class llm_call:
    def __init__(self,choose_llm):
        self.choose_llm = choose_llm
    def select_llm_model(self):
        if self.choose_llm.lower()=="groq":
            return self.groq_chat()
        if self.choose_llm.lower()=="anthropic":
            return self.anthropic_chat()
    def groq_chat(model,**kwarg):
        model = ChatGroq(**kwarg)
        return model
    def anthropic_chat(model,**kwarg):
        model =ChatAnthropic(**kwarg)
        return model




