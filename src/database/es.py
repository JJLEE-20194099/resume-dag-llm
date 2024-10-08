import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch, helpers
import time
import json
import traceback
import simplejson
from ast import literal_eval

from src.clients.discord_client import DiscordClient
from src.utils.none import nan_2_none

load_dotenv(override=True)


cv_mappings = {
    "properties": {
        "batch_id": {"type": "text"},
        "organization": {"type": "text"},
        "major": {"type": "text"},
        "gpa": {"type": "text"},
        "name": {"type": "text"},
        "skill": {"type": "text"},
        "gender": {"type": "text"},
        "job_title": {"type": "text"},
        "phone": {"type": "text"},
        "education": {"type": "text"},
    }
}

class Elastic_search:
    def __init__(self) -> None:
        self.__elastic_url = os.getenv("ELASTIC_URL")
        self.___username = os.getenv("ELASTIC_USERNAME")
        self.__password = os.getenv("ELASTIC_PASSWORD")
        self.__timeout = 30
        self.es_client = Elasticsearch(
                self.__elastic_url,
                http_auth=(self.___username, self.__password),
                timeout = self.__timeout
            )

        try:
            self.es_client.indices.put(index = "cv_data", mappings = cv_mappings)
        except: pass

    def get_data(self) :
        pass

    def set_data(self):
        pass

    def add_a_new_document(self,index, data) :
        self.es_client.index(
            index=index,
            body=data
        )

    def update_current_document(self, index, data, document_id):
        self.es_client.update(index=index, id=document_id, body={ "doc" : data})

    def find_documents(self, index, body):
        doc = self.es_client.search(body, index = index)
        return doc
    def generate_cv_data(self, document, index, ids):
        for _id, record in zip(ids, document):
            return_data = {
                "_op_type": 'update',
                "_index": index,
                "_id": _id,
                "doc": nan_2_none(record),
                "doc_as_upsert": True
            }
            yield return_data

    def update_cv_data(self, data, ids):
        start_time = time.perf_counter()
        print ("update data start -->>>>>>>>", len(data))
        index = f"cv_data"
        error = []

        helpers.bulk(self.es_client, self.generate_cv_data(data, index, ids))
        stop_time = time.perf_counter()
        print (f"updated all record into elasticsearch sucessfully in {stop_time-start_time} seconds, and got {len(error)} error!!!")
