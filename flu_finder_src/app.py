import sys
import os

# Add the parent directory to sys.path so Python recognizes flu_finder_src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, jsonify
from flask_cors import CORS
from flu_finder_src.utils import data_fetcher as data

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Endpoint for fetching data from the CDC
@app.route('/api/fetch-data', methods=['GET'])
def fetch_data():
    data.download_csv()
    df_sorted = data.get_sorted_dataframe()
    return jsonify({'status': 'Data fetched and processed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
