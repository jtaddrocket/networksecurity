from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.pipeline.training_pipeline import TrainingPipeline

from networksecurity.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constants.training_pipeline import DATA_INGESTION_DATABASE_NAME

from networksecurity.utils.main_utils.utils import load_object

import certifi
ca = certifi.where()

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
import pandas as pd
import pymongo
import sys 
import os 

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGO_URL_KEY")
print(mongo_db_url)

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, 
    allow_credentials = True, 
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    app_run(app, host="localhost", port=8000)

