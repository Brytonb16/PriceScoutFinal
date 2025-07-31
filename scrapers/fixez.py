
from playwright.sync_api import sync_playwright

def scrape_fixez(query):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            search_url = f"https://www.fixez.com/index.php/catalogsearch/result/?q={query}"
            page.goto(search_url, timeout=60000)
            page.wait_for_selector(".product-item-info", timeout=10000)

            items = page.query_selector_all(".product-item-info")
            for item in items:
                title_el = item.query_selector(".product-item-link")
                price_el = item.query_selector(".price")
                image_el = item.query_selector("img")

                if not title_el or not price_el:
                    continue

                title = title_el.inner_text().strip()
                link = title_el.get_attribute("href")
                price_text = price_el.inner_text().replace("$", "").strip()
                image = image_el.get_attribute("src") if image_el else ""

                price = float(price_text) if price_text.replace(".", "", 1).isdigit() else None
                if price is None:
                    continue

                results.append({
                    "title": title,
                    "price": price,
                    "source": "Fixez",
                    "in_stock": True,
                    "link": link,
                    "image": image,
                })

        except Exception as e:
            print(f"[Fixez Error] {e}")
        finally:
            browser.close()
    return results
