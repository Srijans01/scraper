import requests
from bs4 import BeautifulSoup
from .models import Product
from .database import Database

class Scraper:
    def __init__(self, num_pages, proxy=None):
        self.num_pages = num_pages
        self.proxy = proxy
        self.database = Database()

    def fetch_page(self, url):
        try:
            response = requests.get(url, proxies={"http": self.proxy, "https": self.proxy} if self.proxy else None)
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            return None

    def scrape(self):
        base_url = 'https://example.com/catalogue?page='
        scraped_count = 0

        for page in range(1, self.num_pages + 1):
            url = f"{base_url}{page}"
            page_content = self.fetch_page(url)
            if not page_content:
                continue

            soup = BeautifulSoup(page_content, 'html.parser')
            products = soup.find_all('div', class_='product')

            for product in products:
                product_title = product.find('h2').text
                product_price = float(product.find('span', class_='price').text.replace('$', ''))
                image_url = product.find('img')['src']

                product_data = Product(product_title=product_title, product_price=product_price, path_to_image=image_url).dict()
                self.database.update_product(product_data)
                scraped_count += 1

        return scraped_count
