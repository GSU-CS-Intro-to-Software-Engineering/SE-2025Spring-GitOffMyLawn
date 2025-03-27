import sys
import os

# Add the parent directory to sys.path so Python recognizes flu_finder_src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flu_finder_src.utils.data_fetcher import download_csv
download_csv()

from flask import Flask
from flask_cors import CORS
from flu_finder_src.routes.api import api_bp

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Register Blueprints
app.register_blueprint(api_bp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
