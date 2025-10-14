import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
import logging

logging.basicConfig(filename='training.log', level=logging.INFO)
logging.info('Loading test data...')
data = pd.read_csv('data/sample.csv')
X = data[['feature1', 'feature2']]
y = data['label']

logging.info('Loading trained model...')
model = joblib.load('model.pkl')

logging.info('Predicting...')
predictions = model.predict(X)
accuracy = accuracy_score(y, predictions)
logging.info(f'Model Accuracy: {accuracy}')
print(f'Model Accuracy: {accuracy}')
