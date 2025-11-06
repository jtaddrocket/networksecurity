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

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData" # the name of the MongoDB collection.
DATA_INGESTION_DATABASE_NAME: str = "TIENDAT" # the database name
DATA_INGESTION_DIR_NAME: str = "data_ingestion" # sub-directory inside Artifacts for this stage.
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" # where processed data ready for modeling is stored.
DATA_INGESTION_INGESTED_DIR: str = "ingested" # directory containing split train/test data.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME 
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# KNN Imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform"
}

"""
Model Trainer related constant start with MODEL_TRAINER VAR NAME 
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD: float = 0.05