from src.config.configuration import *
from src import logger
from src.exception import *
import pandas as pd
from sklearn.model_selection import train_test_split

DataPath='C:\\Users\\Gunja\\Desktop\\Bike_share\\data\\day.csv'

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logger.info('Data Ingestion method starts')

        try:
            df=pd.read_csv(os.path.join(DataPath))
            logger.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            df.drop(columns=['casual','registered','instant','dteday','yr'],inplace=True,axis=1)

            logger.info('Raw data is created')

            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logger.info('Ingestion of Data is completed')

            return(
                train_set,
                test_set)

        except Exception as e:
            logger.info('Exception occured at Data Ingestion Stage')
            raise CustomException(e,sys)