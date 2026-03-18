import pandas as pd

# Load dataset
df = pd.read_csv("data/crime_data.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

# Extract time features
df['Hour'] = df['Date'].dt.hour
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day_name()

# Remove rows without coordinates
df = df.dropna(subset=['Latitude','Longitude'])

# Reduce dataset size to 100k rows (important for memory)
df = df.sample(n=20000, random_state=42)

# Save cleaned dataset
df.to_csv("data/cleaned_crime_data.csv", index=False)

print("Data preprocessing completed")