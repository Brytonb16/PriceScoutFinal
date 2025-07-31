from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import traceback

# Import your real scraper functions
from scrapers.mobile_sentrix import scrape_mobile_sentrix
from scrapers.fixez import scrape_fixez
from scrapers.mengtor import scrape_mengtor
from scrapers.laptopscreen import scrape_laptopscreen

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/search")
def search():
    query = request.args.get("q", "").strip()
    in_stock = request.args.get("inStock", "false").lower() == "true"

    print(f"\n=== New Search ===\nQuery: {query}\nIn-Stock Only: {in_stock}")

    all_results = []

    try:
        results = scrape_mobile_sentrix(query)
        print(f"MobileSentrix returned {len(results)} results")
        all_results.extend(results)
    except Exception as e:
        print("Error in MobileSentrix scraper:")
        traceback.print_exc()

    try:
        results = scrape_fixez(query)
        print(f"Fixez returned {len(results)} results")
        all_results.extend(results)
    except Exception as e:
        print("Error in Fixez scraper:")
        traceback.print_exc()

    try:
        results = scrape_mengtor(query)
        print(f"Mengtor returned {len(results)} results")
        all_results.extend(results)
    except Exception as e:
        print("Error in Mengtor scraper:")
        traceback.print_exc()

    try:
        results = scrape_laptopscreen(query)
        print(f"Laptopscreen returned {len(results)} results")
        all_results.extend(results)
    except Exception as e:
        print("Error in Laptopscreen scraper:")
        traceback.print_exc()

    if in_stock:
        all_results = [item for item in all_results if item.get("in_stock")]

    print(f"Returning {len(all_results)} results\n")
    return jsonify(all_results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
