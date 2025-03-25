import folium
import os
import json

# Initialize empty map with default zoom 5
def initialize_map(location=None, zoom_start=5, geojson_path="flu_finder_src/data/geojson-counties-fips.json"):
    if location is None:
        # Default map location coordinates (US)
        location = [37.0902, -95.7129]

    # Create map centered at location
    m = folium.Map(location=location, zoom_start=zoom_start)

    if os.path.exists(geojson_path):
        with open(geojson_path, "r") as f:
            county_geojson = json.load(f)

            # Add county borders layer
            folium.GeoJson(
                county_geojson,
                name="County Borders",
                tooltip=folium.GeoJsonTooltip(fields=["NAME"], aliases=["County:"]),
                style_function=lambda feature: {
                    "fillColor": "none",
                    "color": "blue",
                    "weight": 1,
                }
            ).add_to(m)
    else:
        print(f"GeoJSON file not found: {geojson_path}")

    return m



# from flu_finder_src.utils.map_visualizer import initialize_map

# Initialize the map
my_map = initialize_map()

# Save the map as an HTML file
my_map.save("test_map.html")

print("Map has been saved as test_map.html")

