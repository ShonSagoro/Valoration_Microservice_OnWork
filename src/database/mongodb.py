import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Database:
    def __init__(self):
        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASS')
        db_name = os.getenv('MONGO_DB_NAME')
        host = os.getenv('MONGO_HOST')
        self.mongo_uri = f"mongodb://{user}:{password}@{host}:27017"
        self.client = AsyncIOMotorClient(self.mongo_uri)

    async def init_db(self, document_models):
        await init_beanie(database=self.client[os.getenv('MONGO_DB_NAME')], document_models=document_models)
