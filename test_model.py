# test_model.py

# Step 1: Set UTF-8 safe stdout
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Step 2: Start appending to the log safely
print("🔍 Testing model...")
with open("train_output.log", "a", encoding="utf-8") as f:
    f.write("\nTesting started...\n")

# Step 3: Your existing imports and code
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Example test
X_test = np.array([[6], [7], [8]])
y_pred = 2 * X_test

# Step 4: Append testing results to the same log
with open("train_output.log", "a", encoding="utf-8") as f:
    f.write("Testing results:\n")
    for i, val in enumerate(X_test):
        f.write(f"Input: {val[0]}, Predicted: {y_pred[i][0]}\n")

print("✅ Testing complete! Logs appended to train_output.log")
