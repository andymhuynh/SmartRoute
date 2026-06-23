import folium


def create_route_map(start_lat, start_lon, end_lat, end_lon, route_coordinates, distance_meters):
    center_lat = (start_lat + end_lat) / 2
    center_lon = (start_lon + end_lon) / 2

    route_map = folium.Map(location=[center_lat, center_lon], zoom_start=15)

    folium.Marker([start_lat, start_lon], popup="Start", tooltip="Start").add_to(route_map)
    folium.Marker([end_lat, end_lon], popup="End", tooltip="End").add_to(route_map)

    folium.PolyLine(
        route_coordinates,
        weight=5,
        tooltip=f"Distance: {distance_meters:.2f} meters"
    ).add_to(route_map)

    return route_map
