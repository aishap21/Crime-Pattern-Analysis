import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import joblib

df = pd.read_csv("data/crime_clusters.csv")

df = df.dropna()

features = df[['Latitude','Longitude','Hour','Month']]
target = df['Primary Type']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
print("F1 Score:", f1_score(y_test, pred, average='macro'))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))

joblib.dump(model, "model.pkl")
print("Model saved successfully")
