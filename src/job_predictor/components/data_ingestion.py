from src.job_predictor.entity.config_entity import DataIngestionConfig
from src.job_predictor.utils.common import create_directory
import gdown
import os

class DataIngestion:
  def __init__(self,config:DataIngestionConfig):
    self.config=config
    create_directory(self.config.root_dir)
    create_directory(self.config.ingested_data_path)

  def download_file_from_drive(self):
    # Ensure the destination folder exists
    drive_url=self.config.url
    destination_folder=self.config.ingested_data_path
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Extract the file ID from the Google Drive URL
    file_id = drive_url.split('/')[-2]

    # Construct the direct download URL
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    # Specify the destination path
    destination_path = os.path.join(destination_folder, "data" + '.csv')  # or choose your file's extension

    # Download the file
    gdown.download(download_url, destination_path, quiet=False)

    print(f"File downloaded to {destination_path}")
