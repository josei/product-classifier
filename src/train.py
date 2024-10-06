from model import Model, save_model
from dataset import train_test_datasets

def train_model():
    model = Model()

    X_train, X_test, y_train, y_test = train_test_datasets(model)
    
    print("Training model...")
    model.fit(X_train, y_train)

    print("Saving model...")
    save_model(model)

    print('Performance on training set:')
    model.evaluate(X_train, y_train)

    print('Performance on test set:')
    model.evaluate(X_test, y_test)
