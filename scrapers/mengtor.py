
from playwright.sync_api import sync_playwright

def scrape_mengtor(query):
    # This should be replaced with real scraping logic
    return [{
        "title": "Mengtor Result for '{}'".format(query),
        "price": 19.99,
        "in_stock": True,
        "source": "Mengtor",
        "link": "https://mengtor.com/search?q=" + query,
        "image": "https://via.placeholder.com/100"
    }]
