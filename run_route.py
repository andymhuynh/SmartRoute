from src.routing import load_graph, shortest_route, get_route_coordinates, estimate_travel_time
from src.map_viz import create_route_map

PLACE = "San Jose State University, San Jose, California, USA"

START_LAT, START_LON = 37.3352, -121.8811
END_LAT, END_LON = 37.3318, -121.8863

graph = load_graph(PLACE, network_type="walk")

route, distance = shortest_route(
    graph,
    START_LAT,
    START_LON,
    END_LAT,
    END_LON,
)

route_coordinates = get_route_coordinates(graph, route)
time_minutes = estimate_travel_time(distance)

route_map = create_route_map(
    START_LAT,
    START_LON,
    END_LAT,
    END_LON,
    route_coordinates,
    distance,
)

route_map.save("outputs/route_map.html")

print(f"Route distance: {distance:.2f} meters")
print(f"Estimated walking time: {time_minutes:.1f} minutes")
print("Saved to outputs/route_map.html")
