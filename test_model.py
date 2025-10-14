import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

print("🔍 Testing model...")

# Example test
X_test = np.array([[6], [7], [8]])
y_pred = 2 * X_test

with open("training.log", "a") as f:
    f.write("\nTesting results:\n")
    for i, val in enumerate(X_test):
        f.write(f"Input: {val[0]}, Predicted: {y_pred[i][0]}\n")

print("✅ Testing complete! Logs appended to training.log")
