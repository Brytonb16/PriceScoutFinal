
from playwright.sync_api import sync_playwright

def scrape_mobile_sentrix(query):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            search_url = f"https://www.mobilesentrix.com/catalogsearch/result/?q={query}"
            page.goto(search_url, timeout=60000)
            page.wait_for_selector(".product-item-info", timeout=10000)

            items = page.query_selector_all(".product-item-info")
            for item in items:
                title = item.query_selector(".product.name a").inner_text().strip()
                price_text = item.query_selector(".price").inner_text().replace("$", "").strip()
                link = item.query_selector(".product.name a").get_attribute("href")
                image = item.query_selector("img").get_attribute("src")

                price = float(price_text) if price_text.replace(".", "", 1).isdigit() else None
                if price is None:
                    continue

                results.append({
                    "title": title,
                    "price": price,
                    "source": "MobileSentrix",
                    "in_stock": True,
                    "link": link,
                    "image": image,
                })

        except Exception as e:
            print(f"[MobileSentrix Error] {e}")
        finally:
            browser.close()
    return results
