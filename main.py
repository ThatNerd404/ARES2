import logging
from logging.handlers import RotatingFileHandler
import os
from recommender import Recommender

def main():
    
    # Setup logger and rotating file handler
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(
    os.path.join("Logs","log.log"), maxBytes=100000, backupCount=5, encoding="utf-8")
    formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',"%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    R = Recommender(logger)

if __name__ == "__main__":
    main()
