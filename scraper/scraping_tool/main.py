from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional
from .models import ScrapeRequest, ScrapeResponse
from .scraper import Scraper

app = FastAPI()

def get_token_header(x_token: str = Header(...)):
    if x_token != "srijan":
        raise HTTPException(status_code=400, detail="Invalid Token")

@app.post("/scrape", response_model=ScrapeResponse, dependencies=[Depends(get_token_header)])
def scrape(request: ScrapeRequest):
    scraper = Scraper(num_pages=request.num_pages, proxy=request.proxy)
    products_scraped = scraper.scrape()
    return ScrapeResponse(products_scraped=products_scraped, status="Scraping Completed")
