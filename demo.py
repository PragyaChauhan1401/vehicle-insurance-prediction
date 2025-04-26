# from src.logger import logging
# logging.debug("this is examples")
from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()