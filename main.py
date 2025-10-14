import time
import numpy as np
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# your existing imports and code below
print("\U0001f680 Training started...")

from sklearn.linear_model import LinearRegression

print("🚀 Training started...")

# Dummy data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

# Save training info to log
with open("training.log", "w") as f:
    f.write("Training completed successfully.\n")
    f.write(f"Coefficient: {model.coef_[0]}\n")
    f.write(f"Intercept: {model.intercept_}\n")

print("✅ Training complete! Log written to training.log")
