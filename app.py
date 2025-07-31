from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
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
    query = request.args.get("q", "")
    in_stock = request.args.get("inStock", "false") == "true"

    print(f"[SEARCH] Query: '{query}', In Stock Only: {in_stock}")

    all_results = []

    try:
        all_results += scrape_mobile_sentrix(query)
    except Exception as e:
        print(f"[MobileSentrix ERROR] {e}")

    try:
        all_results += scrape_fixez(query)
    except Exception as e:
        print(f"[Fixez ERROR] {e}")

    try:
        all_results += scrape_mengtor(query)
    except Exception as e:
        print(f"[Mengtor ERROR] {e}")

    try:
        all_results += scrape_laptopscreen(query)
    except Exception as e:
        print(f"[Laptopscreen ERROR] {e}")

    # Optional: Filter by stock
    if in_stock:
        all_results = [item for item in all_results if item.get("in_stock")]

    return jsonify(all_results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
