from pydantic import BaseModel
from typing import List

# Input product class
class InputProduct(BaseModel):
    also_buy: List[str]
    also_view: List[str]
    asin: str
    brand: str
    description: list
    feature: List[str]
    image: list
    price: str
    title: str

    def text(self):
        return f"{self.brand} {self.title} {' '.join(self.description)} {' '.join(self.feature)}"

# Full product class, including categories
class Product(InputProduct):
    category: List[str] = []
    main_cat: str

# Output from REST API
class ProductCategory(BaseModel):
    main_cat: str
