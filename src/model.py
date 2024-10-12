import os
import re
import pickle
from itertools import islice
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestCentroid
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from model2vec import StaticModel
# from sentence_transformers import SentenceTransformer

MODEL_PATH = os.path.abspath('models/model.pkl')

embedder = None
def get_embedder():
    global embedder
    if embedder is None: embedder = StaticModel.from_pretrained("minishlab/M2V_base_output")
    # if embedder is None: embedder = SentenceTransformer('baai/bge-base-en-v1.5')
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
            # ('classifier', KNeighborsClassifier())
        ])

    # Prepare data by splitting into train and test
    def prepare(self, products):
        dataset = []
        for chunk in iter(lambda: list(islice(products, 512)), []):
            inputs = self.clean(chunk)
            for k, product in enumerate(chunk):
                output = product.main_cat
                dataset.append([inputs[k], output])

        X_train, X_test, y_train, y_test = train_test_split(
            [sample[0] for sample in dataset],
            [sample[1] for sample in dataset],
            test_size=0.3,
        )

        return X_train, X_test, y_train, y_test
    
    # Preprocess products by parsing price and applying embedding model
    def clean(self, products):
        embeddings = get_embedder().encode([product.text() for product in products])
        prices = [[float(product.price[1:])] if re.match(r'^\$\d+(\.\d{2})?$', product.price) else [0] for product in products]
        return np.append(np.array(embeddings), np.array(prices), axis=1)

    # Fit by standardising data and using a nearest centroid classifier
    def fit(self, X, y):
        self.pipeline.fit(X, y)

    # Evaluate performance on a data set
    def evaluate(self, X, y):
        y_pred = self.pipeline.predict(X)
        print(classification_report(y, y_pred))

    # Predict on non-clean samples (embeddings need to be computed, price needs to be parsed)
    def predict(self, products):
        X = self.clean(products)
        return self.pipeline.predict(X)
