
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from scrapers.mobile_sentrix import scrape_mobile_sentrix
from scrapers.fixez import scrape_fixez
from scrapers.mengtor import scrape_mengtor
from scrapers.laptopscreen import scrape_laptopscreen

app = Flask(__name__)
CORS(app)

@app.route("/api/search")
def search():
    query = request.args.get("q", "")
    in_stock = request.args.get("inStock", "false") == "true"

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
    
    return jsonify(all_results)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
