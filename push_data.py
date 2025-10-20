import os 
import sys 
import json 

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")


import certifi #-> The certifi library helps Python verify that the website or API you are accessing has a valid SSL certificate
ca=certifi.where() #-> The certifi.where() function returns the absolute path to the .pem file containing Mozilla's root certificate (CA bundle) list.

import pymongo
import pandas as pd 
import numpy as np 
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    """
    Input: 
              name   age
        0    Alice   24
        1      Bob   30
        2  Charlie   18
    
    Output:
        [
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 18}
        ]
    """
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop = True, inplace = True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection 
            self.records = records 
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__=='__main__':
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "TIENDAT"
    Collection ="NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)