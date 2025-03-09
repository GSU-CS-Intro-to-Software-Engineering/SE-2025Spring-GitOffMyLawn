import folium

# Initialize empty map with default zoom 5
def initialize_map(location=None, zoom_start=5):

    if location is None:
        # Default map location coordinates (US)
        location = [37.0902, -95.7129]

    # Create map centered at location
    m = folium.Map(location=location, zoom_start=zoom_start)
    return m



# # test_map.py
# from flu_finder_src.routes.map_visualizer import initialize_map

# # Initialize the map
# my_map = initialize_map()

# # Save the map as an HTML file
# my_map.save("test_map.html")

# print("Map has been saved as test_map.html")

