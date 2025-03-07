from src.job_predictor import CustomLogger
from src.job_predictor.pipeline.data_ingestion_pipeline import DataIngestionPipeline
logger=CustomLogger().get_logger()

logger.info("Logger Intialised")
logger.info("Data Ingestion Started!")
data_ingestion=DataIngestionPipeline()
data_ingestion.data_ingestion()
logger.info("Data Ingestion Done!")
logger.warning("Logger Terminated")