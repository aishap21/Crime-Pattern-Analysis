import pandas as pd

df = pd.read_csv("data/crime_data.csv")

df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

df['Hour'] = df['Date'].dt.hour
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day_name()

df = df.dropna(subset=['Latitude','Longitude'])

df = df.sample(n=20000, random_state=42)

df.to_csv("data/cleaned_crime_data.csv", index=False)

print("Data preprocessing completed")
