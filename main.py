# main.py

# Step 1: Set UTF-8 encoding for safe printing
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Step 2: Start log file
print("🚀 Training started...")
with open("train_output.log", "w", encoding="utf-8") as f:
    f.write("Training started...\n")

# Step 3: Your existing imports and training code
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# Step 4: Dummy training logic (replace with your real code)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

# Step 5: Save training info to the log
with open("train_output.log", "a", encoding="utf-8") as f:
    f.write("Training completed successfully.\n")
    f.write(f"Coefficient: {model.coef_[0]}\n")
    f.write(f"Intercept: {model.intercept_}\n")

print("✅ Training complete! Log written to train_output.log")
