import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("C:/Users/siddhesh1290/NetTwin-Security/dataset/data.csv", header=None)
data.columns = ["frame_len","ip_src","ip_dst","dst_port","label"]

# Convert IP to numeric
data["ip_src"] = data["ip_src"].astype("category").cat.codes
data["ip_dst"] = data["ip_dst"].astype("category").cat.codes

X = data[["frame_len","ip_src","ip_dst","dst_port"]]
y = data["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ids_model.pkl")

print("Model trained and saved as ids_model.pkl")
