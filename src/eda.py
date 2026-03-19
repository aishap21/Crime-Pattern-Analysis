import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_crime_data.csv")

sns.countplot(y=df['Primary Type'])
plt.title("Crime Type Distribution")
plt.show()

sns.histplot(df['Hour'], bins=24)
plt.title("Crime by Hour")
plt.show()
