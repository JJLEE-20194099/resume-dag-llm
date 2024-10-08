import pymongo
import os
from dotenv import load_dotenv
import traceback

load_dotenv(override=True)

class Mongodb():
    __connection_str : str
    __client : None
    __database : None
    __collection : None

    def __init__(self):
        self.connection_str = os.getenv("MONGODB_CONNECTION_STRING")
        self.__client = pymongo.MongoClient(self.connection_str)
        self.__database = self.__client[os.getenv("CV_MONGO_DATABASE")]

        print(os.getenv("MONGODB_CONNECTION_STRING"), os.getenv("CV_MONGO_DATABASE"))

    def get_collection(self, collection_name:str):
        return self.__database[collection_name]




