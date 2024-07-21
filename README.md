# scraper

# FastAPI Scraping Tool

## Project Overview

This project is a web scraping tool built with the FastAPI framework. It automates the process of scraping product information from a target website, including the product name, price, and image. The scraped data is stored locally in a JSON file, with the ability to easily switch to other storage solutions. The tool is designed to be flexible, with options to limit the number of pages scraped and use a proxy for the requests.

## Features

- **Scrape Product Data**: Extracts product name, price, and image URL from multiple pages of the target website.
- **Configurable Settings**: Limit the number of pages to scrape and optionally use a proxy server.
- **Data Storage**: Stores scraped data locally in a JSON file with an easy path for future storage enhancements.
- **Authentication**: Simple token-based authentication to secure the scraping endpoint.
- **Notification**: Prints the number of products scraped to the console after each run, with the potential to expand to other notification methods.
- **Retry Mechanism**: Simple retry logic to handle temporary site issues.
- **In-Memory Caching**: Uses an in-memory database to avoid updating unchanged product prices.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-scraping-tool.git
    cd fastapi-scraping-tool
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Start the FastAPI application:
    ```bash
    uvicorn scraping_tool.main:app --reload
    ```

2. Send a POST request to the `/scrape` endpoint with the necessary headers and body. For example, using `curl`:
    ```bash
    curl -X POST "http://127.0.0.1:8000/scrape" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "x-token: your_static_token" \
    -d '{"num_pages": 5, "proxy": ""}'
    ```

3. The scraped data will be stored in a JSON file named `products.json` in the project directory.

### Example JSON Output

```json
[
    {
        "product_title": "Example Product 1",
        "product_price": 29.99,
        "path_to_image": "https://example.com/image1.jpg"
    },
    {
        "product_title": "Example Product 2",
        "product_price": 49.99,
        "path_to_image": "https://example.com/image2.jpg"
    }
]
