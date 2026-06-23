import osmnx as ox
import networkx as nx
import folium

PLACE = "San Jose, California, USA"

START_LAT, START_LON = 37.3352, -121.8811
END_LAT, END_LON = 37.3318, -121.8863

print("Downloading street network...")
G = ox.graph_from_place(PLACE, network_type="walk")

print("Finding nearest nodes...")
start_node = ox.distance.nearest_nodes(G, START_LON, START_LAT)
end_node = ox.distance.nearest_nodes(G, END_LON, END_LAT)

print("Computing shortest path...")
route = nx.shortest_path(G, start_node, end_node, weight="length")

distance = nx.shortest_path_length(
    G,
    start_node,
    end_node,
    weight="length"
)

print(f"Distance: {distance:.2f} meters")

route_coords = [
    (G.nodes[node]["y"], G.nodes[node]["x"])
    for node in route
]

m = folium.Map(
    location=[START_LAT, START_LON],
    zoom_start=15
)

folium.Marker(
    [START_LAT, START_LON],
    popup="Start"
).add_to(m)

folium.Marker(
    [END_LAT, END_LON],
    popup="End"
).add_to(m)

folium.PolyLine(
    route_coords,
    weight=5
).add_to(m)

m.save("outputs/first_route.html")

print("Map saved!")