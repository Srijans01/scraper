from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_title: str
    product_price: float
    path_to_image: str

class ScrapeRequest(BaseModel):
    num_pages: int
    proxy: Optional[str] = None

class ScrapeResponse(BaseModel):
    products_scraped: int
    status: str
