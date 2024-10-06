from fastapi import FastAPI
from classes import InputProduct, ProductCategory
from model import load_model

app = FastAPI(title="Product Classifier API")
model = load_model()

@app.get("/")
def ping():
    return {"ping": "pong"}

@app.post("/predict", response_model=ProductCategory)
def predict(product: InputProduct):
    prediction = model.predict(product)
    return ProductCategory(main_cat=prediction)
