from src.job_predictor.config.configuration import ConfigurationManager
from src.job_predictor.components.data_ingestion import DataIngestion

# Data Ingestion Pipeline
import warnings
warnings.simplefilter("ignore")
config=ConfigurationManager()

class DataIngestionPipeline:
    def __init__(self):
        pass

    def data_ingestion(self):
        data_ingestion_config=config.DataIngestionManager()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.download_file_from_drive()