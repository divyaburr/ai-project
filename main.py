import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import logging

# Setup logging
logging.basicConfig(filename='training.log', level=logging.INFO)
logging.info('Loading dataset...')
data = pd.read_csv('data/sample.csv')

X = data[['feature1', 'feature2']]
y = data['label']

logging.info('Splitting dataset...')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logging.info('Training model...')
model = LogisticRegression()
model.fit(X_train, y_train)

logging.info('Saving model...')
joblib.dump(model, 'model.pkl')
logging.info('Training completed successfully!')
print("Training completed!")
