from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

df = pd.read_csv("data/cleaned_crime_data.csv")
df = df.sample(n=10000)

coords = df[['Latitude','Longitude']]

model = KMeans(n_clusters=5)
labels = model.fit_predict(coords)

score = silhouette_score(coords, labels)

print("Silhouette Score:", score)