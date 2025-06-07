from langchain_huggingface import HuggingFaceEmbeddings

class Embedding_model:
    def __init__(self,embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
        self.embedding_model = embedding_model
    def create_embedding(self,data):
        embedding_model = HuggingFaceEmbeddings(model_name = self.embedding_model)
        return embedding_model


