import os 
import sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils2 import dump_csv_file_to_mongodb_collection
from sensor.pipeline.training_pipeline import TrainPipeline



# def test_exception():
#     try:
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 
    

if __name__=="__main__":
    # file_path = "C:/Users/praja\Live-Sensor/aps_failure_training_set1.csv"
    # database = "MyDataBase"
    # collection = "Sensor"
    # dump_csv_file_to_mongodb_collection(file_path=file_path,database_name=database,collection_name=collection)
    

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()


    