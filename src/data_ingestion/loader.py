import logging
import pandas as pd
import os
from pathlib import path
class DataIngester:
    logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
    logging.info("starting data ingetion process")
    def __init__(self,data_path):
        if os.path.exists(self.data_path):
            self.data_path = path(data_path)
    def check_file_folder(self):
        if self.data_path.is_file():
            return self.load_csv_file(self.data_path)
        if self.data_path.is_dir():
            return self.load_folder(self.data_path)
    def load_csv_file(self):
        try:
            if self.data_path.endswith(".csv"):
                csv_data = pd.read_csv(self.path)
                return csv_data
        except Exception as e:
            logging.info(f"error occured {e}")

    def load_folder(self):
        try:
            file_list = [file for file in os.listdir(self.data_path) if file.endswith(".csv")]
            if len(file_list)>0:
                for file_name in file_list:
                    final_file_path = os.path.join(self.data_path,file_name)
                    current_data = pd.read_csv(final_file_path)
                    yield current_data
            else:
                logging.info("No file exist in folder, Please provide correct folder or file")
        except Exception as e:
            logging.info(f"error occured while loading file {e}")
            
