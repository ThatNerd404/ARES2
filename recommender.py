import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

class Recommender():
    def __init__(self):
        #self.logger = logger
        #self.logger.debug("Finished Initialization")
        self.dataset = pd.read_csv(os.path.join("datasets","data.csv"))
        features = self.dataset[["danceability", "energy", "tempo", "valence","instrumentalness","speechiness","acousticness","liveness","loudness"]].dropna()

        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)

        self.similarity = cosine_similarity(scaled_features)


    def recommend(self,song_name,n=1):
        try:
            idx = self.dataset[self.dataset['name'].str.lower() == song_name.lower()].index[0]
        except IndexError:
            print("Song not found.")
            return
    
        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]
    
        print(f"\nBecause you like **{self.dataset.iloc[idx]['name']} - {self.dataset.iloc[idx]['artists']}**, you may also like:")
        for i, score in scores:
            print(" →", self.dataset.iloc[i]['name'], "-", self.dataset.iloc[i]['artists'])
if __name__ == "__main__":
    R = Recommender()
    R.recommend("Shape of You")

