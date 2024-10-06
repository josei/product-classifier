import os
import json
import gzip
import numpy as np
from classes import Product

dataset_file = os.path.abspath('data/amz_products_small.jsonl.gz')
x_train_file = os.path.abspath('data/x_train.npy')
x_test_file = os.path.abspath('data/x_test.npy')
y_train_file = os.path.abspath('data/y_train.npy')
y_test_file = os.path.abspath('data/y_test.npy')

def parse(path):
    g = gzip.open(path, 'r')
    i = 0
    for l in g:
        i += 1
        if i % 1000 == 0: print('.', end='', flush=True)
        yield Product(**json.loads(l))
    print()

def read_dataset():
    if not os.path.exists(dataset_file):
        raise Exception('Dataset https://drive.google.com/file/d/1Zf0Kdby-FHLdNXatMP0AD2nY0h-cjas3/view?usp=sharing needs to be downloaded and included into the `data` folder.')
    
    return parse(dataset_file)

def train_test_datasets(model):
    if os.path.exists(x_train_file):
        print("Loading dataset...")
        X_train = np.load(x_train_file)
        X_test = np.load(x_test_file)
        y_train = np.load(y_train_file)
        y_test = np.load(y_test_file)
    else: 
        print("Preparing dataset...", end='', flush=True)
        X_train, X_test, y_train, y_test = model.prepare(read_dataset())
        np.save(x_train_file, X_train)
        np.save(x_test_file, X_test)
        np.save(y_train_file, y_train)
        np.save(y_test_file, y_test)

    return X_train, X_test, y_train, y_test
