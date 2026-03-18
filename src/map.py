import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv("data/crime_clusters.csv")

m = folium.Map(location=[41.87, -87.62], zoom_start=10)

heat_data = df[['Latitude','Longitude']]

HeatMap(heat_data).add_to(m)

m.save("maps/crime_heatmap.html")

print("Map created")