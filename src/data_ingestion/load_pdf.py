from langchain_community.document_loaders import DirectoryLoader,CSVLoader
import os
import logging
from pathlib import Path
import pandas as pd
class Directory_loader:
    logging.basicConfig(level=logging.INFO,format=('%(asctime)s:%(message)s'))
    def __init__(self,data_path):
        self.data_path =data_path   
    def file_filter(self,path)->bool:
        return path.endswith((".txt",'.pdf'))
    
    def route_file_folder(self):
        logging.info("routing file folder")
        try:
            if self.data_path.is_file():
                logging.INFO("got file and serving file")
                if str(self.data_path).endswith(('.txt','.csv')):
                    self.load_files(self.data)          
            
            if self.data_path.is_dir():
                total_file_count= len(os.listdir(self.data_path))
                usable_file = [file for file in os.listdir(self.data_path) if str(file).endswith((".txt",".csv",".pdf"))]
                final_file_path =[os.path.join(self.data_path,file) for file in usable_file] 
                logging.info(f"Loading directory total file count : {total_file_count} usable file count {len(usable_file)}")
                if len(usable_file)>0:
                    
                    for file_path in final_file_path:
                        print(file_path)
                        if str(file_path).endswith((".pdf",'.txt')):
                                other_data=self.load_directory()
                                print(other_data)
                                return other_data
                        if str(self.data_path).endswith((".csv")):
                            csv_data = self.csv_loader(file_path)
                            print(csv_data)
                            return csv_data
                else:
                    logging.info("0 readable file found")
        
        except Exception as e:
            logging.info(f"getting error like {e}")
            
    def load_files(self):
        pass
    
    def load_directory(self):
        try:
            loader1 = DirectoryLoader(self.data_path,glob="**/*.pdf",recursive=True)
            documents_pdf = loader1.load()
            print(documents_pdf)
            return documents_pdf
            # loader2 = Directory_loader(self.data_path,glob="**/*.txt",recursive=True)
            # load_txt = loader2.load()
            # yield load_txt
        except Exception as e:
            logging.info(f"Got unexpected error {e}")
    def csv_loader(self,file_path):
        document= CSVLoader(file_path)
        csv_data = document.load()
        print(csv_data)
        return csv_data
        


if __name__=="__main__":
    path = Path(r"C:\Users\diwashar\VS_Code_project\eaAi_Agents\data\archive (30)")
    final_data = Directory_loader(path).route_file_folder()

    
            