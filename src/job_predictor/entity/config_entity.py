from pathlib import Path
from dataclasses import dataclass

# Define a data class
@dataclass
class DataIngestionConfig:
  root_dir:Path
  ingested_data_path:Path
  url:str


@dataclass
class DataTransformationConfig:
  raw_data_dir:Path
  transformed_data_dir:Path
  transformed_data:Path

@dataclass
class TrainingConfig:
  data:Path
  test_size:float
  model_dir:Path
  encoder_dir:Path
  vectorizer_dir:Path
  array_dir:Path
  random_state:int
  max_iter:int
  verbose:int
  C:float

@dataclass
class ModelEvaluationConfig:
  model_dir:Path
  report_dir:Path
  array_dir:Path
  best_model_dir:Path