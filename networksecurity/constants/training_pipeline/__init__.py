import os 
import sys 
import numpy as np 
import pandas as pd

"""
Defining common constant variable for training pipeline 
"""
TARGET_COLUMN = "Result" # the label column in dataset, e.g., "Result" for phishing detection.
PIPELINE_NAME: str = "NetworkSecurity" # the name of the overall training pipeline.
ARTIFACT_DIR: str = "Artifacts" # the main folder where all generated files (artifacts) are stored.
FILE_NAME: str = "phisingData.csv" # original dataset filename.

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData" # the name of the MongoDB collection.
DATA_INGESTION_DATABASE_NAME: str = "TIENDAT" # the database name
DATA_INGESTION_DIR_NAME: str = "data_ingestion" # sub-directory inside Artifacts for this stage.
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" # where processed data ready for modeling is stored.
DATA_INGESTION_INGESTED_DIR: str = "ingested" # directory containing split train/test data.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2