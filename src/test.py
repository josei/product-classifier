from model import load_model
from dataset import train_test_datasets

def test_model():
    model = load_model()

    X_train, X_test, y_train, y_test = train_test_datasets(model)

    print('Performance on training set:')
    model.evaluate(X_train, y_train)

    print('Performance on test set:')
    model.evaluate(X_test, y_test)
