from dataclasses import dataclass
import os
import pymongo

@dataclass
class EnvironmentVariale:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariale()

client = pymongo.MongoClient(env_var.mongo_db_url)