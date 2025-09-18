import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("student-mat.csv", sep=";")

# Create Pass/Fail target
data['Pass'] = data['G3'].apply(lambda x: 1 if x >= 10 else 0)

# Select features
features = ["age", "studytime", "failures", "absences", "G1", "G2"]
X = data[features]
y = data["Pass"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "student_model.pkl")
print("✅ Model saved at ml_model/student_model.pkl")
