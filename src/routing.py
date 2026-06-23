import osmnx as ox
import networkx as nx


def load_graph(place: str, network_type: str = "walk"):
    return ox.graph_from_place(place, network_type=network_type)


def get_nearest_node(graph, latitude: float, longitude: float):
    return ox.distance.nearest_nodes(graph, longitude, latitude)


def shortest_route(graph, start_lat, start_lon, end_lat, end_lon):
    start_node = get_nearest_node(graph, start_lat, start_lon)
    end_node = get_nearest_node(graph, end_lat, end_lon)

    route = nx.shortest_path(graph, start_node, end_node, weight="length")
    distance = nx.shortest_path_length(graph, start_node, end_node, weight="length")

    return route, distance


def get_route_coordinates(graph, route):
    return [(graph.nodes[node]["y"], graph.nodes[node]["x"]) for node in route]


def estimate_travel_time(distance_meters: float, speed_kmh: float = 5.0):
    distance_km = distance_meters / 1000
    hours = distance_km / speed_kmh
    return hours * 60
