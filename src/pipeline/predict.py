import sys
import pandas as pd
from src.exception import CustomException
from src import logger
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            model = load_object(file_path=model_path)
            pred = model.predict(features)
            return pred
        except Exception as e:
            logger.info('Exception occured in prediction pipeline')
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 season:int,
                 mnth:int,
                 holiday:int,
                 weekday:int,
                 workingday:int,
                 weathersit:int,
                 temp:float,
                 atemp:float,
                 hum:float,
                 windspeed:float):
        
        self.season=season
        self.mnth=mnth
        self.holiday=holiday
        self.weekday=weekday
        self.workingday=workingday
        self.weathersit=weathersit
        self.temp=temp
        self.atemp=atemp
        self.hum=hum
        self.windspeed=windspeed

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'season':[self.season],
                'mnth':[self.mnth],
                'holiday':[self.holiday],
                'weekday':[self.weekday],
                'workingday':[self.workingday],
                'weathersit':[self.weathersit],
                'temp':[self.temp],
                'atemp':[self.atemp],
                'hum':[self.hum],
                'windspeed':[self.windspeed]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logger.info('Dataframe Gathered')
            return df
        except Exception as e:
            logger.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)