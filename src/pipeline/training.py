import os
import sys
from src import logger
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer

if __name__=='__main__':
    obj=DataIngestion()
    train_arr,test_arr=obj.initiate_data_ingestion()
    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)