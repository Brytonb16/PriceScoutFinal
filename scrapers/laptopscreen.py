
from playwright.sync_api import sync_playwright

def scrape_laptopscreen(query):
    # This should be replaced with real scraping logic
    return [{
        "title": "Laptopscreen Result for '{}'".format(query),
        "price": 19.99,
        "in_stock": True,
        "source": "Laptopscreen",
        "link": "https://laptopscreen.com/search?q=" + query,
        "image": "https://via.placeholder.com/100"
    }]
