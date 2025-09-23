import logging
from logging.handlers import RotatingFileHandler
import pandas as pd
import os
class Recommender():
    def __init__(self):

        # Setup logger and rotating file handler
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        os.system("mkdir -p Logs")
        handler = RotatingFileHandler(
        os.path.join("Logs","log.log"), maxBytes=100000, backupCount=5, encoding="utf-8")
        formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',"%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.logger.debug("Finished Initialization")
        self.dataset = pd.read_csv(os.path.join("datasets","data.csv"))
        print(self.dataset)

if __name__ == "__main__":
    R = Recommender()

