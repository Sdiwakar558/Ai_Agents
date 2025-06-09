from langchain.vectorstores import FAISS
from src.embeddings import embedder
import logging
class Create_vectorstore:
    logging.basicConfig(level=logging.INFO,format = "%(asctime)s:%(message)s")
    def __init__(self,vector_database_path):
        self.vector_database_path = vector_database_path
    
    def create_vector(self,data_chunks,embedding_model):
        try:
            vectorstore = FAISS.from_documents(data_chunks,embedding_model) 
            vectorstore.save_local(self.vector_database_path)
            logging.info(f"Data store to address {self.vector_database_path} in vectorstore")
        except Exception as e:
            logging.info(f"encounter error like {e}")
               
    
            
            