import pandas as pd
from sklearn.cluster import DBSCAN

# Load cleaned data
df = pd.read_csv("data/cleaned_crime_data.csv")

# Reduce dataset to 10000 rows to avoid memory error
df = df.sample(n=10000, random_state=42)

# Take coordinates
coordinates = df[['Latitude','Longitude']]

# Apply DBSCAN
model = DBSCAN(eps=0.01, min_samples=5)
df['Cluster'] = model.fit_predict(coordinates)

# Save clustered data
df.to_csv("data/crime_clusters.csv", index=False)

print("Clustering completed successfully")