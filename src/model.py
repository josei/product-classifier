import os
import re
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestCentroid
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from model2vec import StaticModel

MODEL_PATH = os.path.abspath('models/model.pkl')

embedder = None
def get_embedder():
    global embedder
    if embedder is None: embedder = StaticModel.from_pretrained("minishlab/M2V_base_output")
    return embedder

def save_model(model):
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

class Model:
    def __init__(self):
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('sampler', SMOTE()),
            ('classifier', NearestCentroid())
        ])

    # Prepare data by splitting into train and test
    def prepare(self, products):
        dataset = []
        for product in products:
            dataset.append([self.clean(product), product.main_cat])

        X_train, X_test, y_train, y_test = train_test_split(
            [sample[0] for sample in dataset],
            [sample[1] for sample in dataset],
            test_size=0.3,
        )

        return X_train, X_test, y_train, y_test
    
    # Preprocess a single sample by parsing price and applying embedding model
    def clean(self, product):
        embedding = get_embedder().encode(product.text())
        price = float(product.price[1:]) if re.match(r'^\$\d+(\.\d{2})?$', product.price) else 0
        return np.array([*embedding, price])

    # Fit by standardising data and using a nearest centroid classifier
    def fit(self, X, y):
        self.pipeline.fit(X, y)

    # Evaluate performance on a data set
    def evaluate(self, X, y):
        y_pred = self.pipeline.predict(X)
        print(classification_report(y, y_pred))

    # Predict on a single, non-clean sample (embeddings need to be computed, price needs to be parsed)
    def predict(self, product):
        x = self.clean(product)
        return self.pipeline.predict([x])[0]
