
from playwright.sync_api import sync_playwright

def scrape_laptopscreen(query):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            search_url = f"https://www.laptopscreen.com/English/search/?search_terms={query}"
            page.goto(search_url, timeout=60000)
            page.wait_for_selector("table.tabcontent", timeout=10000)

            rows = page.query_selector_all("table.tabcontent tr")[1:]  # Skip header row
            for row in rows:
                cols = row.query_selector_all("td")
                if len(cols) < 4:
                    continue

                title = cols[0].inner_text().strip()
                price_text = cols[2].inner_text().replace("$", "").strip()
                link_el = cols[0].query_selector("a")
                link = "https://www.laptopscreen.com" + link_el.get_attribute("href") if link_el else ""
                image = "https://www.laptopscreen.com/images/product_photo.png"  # Static image for now

                price = float(price_text) if price_text.replace(".", "", 1).isdigit() else None
                if price is None:
                    continue

                results.append({
                    "title": title,
                    "price": price,
                    "source": "Laptopscreen",
                    "in_stock": True,
                    "link": link,
                    "image": image,
                })

        except Exception as e:
            print(f"[Laptopscreen Error] {e}")
        finally:
            browser.close()
    return results

