import pandas as pd
from sklearn.cluster import DBSCAN

df = pd.read_csv("data/cleaned_crime_data.csv")

df = df.sample(n=10000, random_state=42)

coordinates = df[['Latitude','Longitude']]

model = DBSCAN(eps=0.01, min_samples=5)
df['Cluster'] = model.fit_predict(coordinates)

df.to_csv("data/crime_clusters.csv", index=False)

print("Clustering completed successfully")
