from src.job_predictor.entity.config_entity import DataIngestionConfig
from src.job_predictor.entity.config_entity import DataTransformationConfig
from src.job_predictor.entity.config_entity import ModelEvaluationConfig
from src.job_predictor.entity.config_entity import TrainingConfig
from src.job_predictor.utils.common import create_directory
from src.job_predictor.utils.common import read_yaml


class ConfigurationManager:
  def __init__(self):
    #read yaml files here

    self.config=read_yaml("config/config.yaml")
    self.params=read_yaml("params.yaml")
    self.root_dir=self.config["root"]
    create_directory(self.root_dir)

  def DataIngestionManager(self)->DataIngestionConfig:
    config=self.config["data_ingestion"]
    data_ingestion_config=DataIngestionConfig(
        root_dir=config["root_dir"],
        ingested_data_path=config["ingested_data_path"],
        url=config["url"]
    )
    return data_ingestion_config

  def DataTransformationManager(self)->DataTransformationConfig:
    config=self.config["data_transformation"]
    data_transformation_config=DataTransformationConfig(
        raw_data_dir=config["raw_data_dir"],
        transformed_data_dir=config["transformed_data_dir"],
        transformed_data=config["transformed_data"]
    )
    return data_transformation_config

  def TrainingManager(self)->TrainingConfig:
    config=self.config["training"]
    training_config=TrainingConfig(
        data=config["data"],
        test_size=config["test_size"],
        random_state=config["random_state"],
        max_iter=self.params["max_iter"],
        verbose=self.params["verbose"],
        C=self.params["C"],
        model_dir=config["model_dir"],
        encoder_dir=config["encoder_dir"],
        vectorizer_dir=config["vectorizer_dir"],
        array_dir=config["array_dir"]
    )
    return training_config

  def EvaluationManager(self)->ModelEvaluationConfig:
    config=self.config["evaluation"]
    evaluation_config=ModelEvaluationConfig(
        model_dir=config["model_dir"],
        array_dir=config["array_dir"],
        report_dir=config["report_dir"],
        best_model_dir=config["best_model_dir"]
    )
    return evaluation_config