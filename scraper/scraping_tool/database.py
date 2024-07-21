import json
import os

class Database:
    def __init__(self, file_path='products.json'):
        self.file_path = file_path
        self.products = self.load_products()

    def load_products(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_products(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.products, file, indent=4)

    def update_product(self, product):
        for existing_product in self.products:
            if existing_product['product_title'] == product['product_title']:
                if existing_product['product_price'] != product['product_price']:
                    existing_product['product_price'] = product['product_price']
                    self.save_products()
                return
        self.products.append(product)
        self.save_products()
