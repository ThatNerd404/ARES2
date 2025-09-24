import pandas as pd
import os

class Recommender():
    def __init__(self,logger):
        self.logger = logger
        self.logger.debug("Finished Initialization")
        self.dataset = pd.read_csv(os.path.join("datasets","data.csv"))
        print(self.dataset)
        print(self.dataset.shape)
        print(self.dataset.columns)
        print(self.dataset.info())
        print(self.dataset.describe())

if __name__ == "__main__":
    R = Recommender()

