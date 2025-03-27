from flask import Blueprint, jsonify, request
from flu_finder_src.utils import data_fetcher as data
from flu_finder_src.utils import queries
from flu_finder_src.utils.map_visualizer import initialize_map

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Endpoint for fetching data from the CDC
@api_bp.route('/cdc/data', methods=['GET'])
def fetch_data():
    data.download_csv()
    df_sorted = data.get_sorted_dataframe()
    return jsonify({'status': 'Data fetched and processed successfully'})

# Enpoint for data by country
@api_bp.route('/country/data', methods=['GET'])
def country_data():
    try:
        summary = queries.get_USA_summary()

        return jsonify({
            'status': 'success',
            'summary': summary
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Enpoint for data by state
@api_bp.route('/state/data', methods=['GET'])
def state_data():
    state = request.args.get('state')
    if not state:
        return jsonify({'error': 'Valid State parameter is required'}), 400

    try:
        filtered_data = queries.filter_by_state(state)
        summary = queries.get_state_summary(state)
        result = filtered_data.to_dicts()

        return jsonify({
            'status': 'success',
            'state': state,
            'summary': summary,
            'data': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Enpoint for data by county
@api_bp.route('/county/data', methods=['GET'])
def county_data():
    county = request.args.get('county')
    state = request.args.get('state')
    if not county or not state:
        return jsonify({'error': 'Valid County and State parameters are required'}), 400

    try:
        filtered_data = queries.filter_by_county(county, state)
        summary = queries.get_county_summary(county, state)
        result = filtered_data.to_dicts()

        return jsonify({
            'status': 'success',
            'county': county,
            'state': state,
            'summary': summary,
            'data': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint for initializing the map
@api_bp.route('/map/initialize', methods=['GET'])
def initialize_map_endpoint():
    map_html = initialize_map().get_root().render()
    return jsonify({'map_html': map_html})

