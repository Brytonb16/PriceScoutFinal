
from playwright.sync_api import sync_playwright

def scrape_mobile_sentrix(query):
    # This should be replaced with real scraping logic
    return [{
        "title": "Mobile_sentrix Result for '{}'".format(query),
        "price": 19.99,
        "in_stock": True,
        "source": "Mobile_sentrix",
        "link": "https://mobile_sentrix.com/search?q=" + query,
        "image": "https://via.placeholder.com/100"
    }]
