import streamlit as st
from streamlit_folium import st_folium

from src.routing import load_graph, shortest_route, get_route_coordinates, estimate_travel_time
from src.map_viz import create_route_map

st.set_page_config(page_title="SmartRoute", layout="wide")

st.title("SmartRoute")
st.write("A graph-based route optimization app using OpenStreetMap, OSMnx, NetworkX, and Streamlit.")

SJSU_LOCATIONS = {
    "MLK Library": (37.3354, -121.8851),
    "Student Union": (37.3366, -121.8807),
    "Engineering Building": (37.3376, -121.8813),
    "Duncan Hall": (37.3372, -121.8815),
    "Spartan Recreation Center": (37.3350, -121.8797),
    "San Jose City Hall": (37.3379, -121.8863),
    "Cesar Chavez Monument": (37.3352, -121.8811),
}

start_name = st.selectbox("Start Location", list(SJSU_LOCATIONS.keys()), index=0)
end_name = st.selectbox("End Location", list(SJSU_LOCATIONS.keys()), index=1)
network_type = st.selectbox("Travel Mode", ["walk", "drive", "bike"], index=0)
speed_kmh = st.slider("Estimated speed in km/h", 1.0, 120.0, 5.0)

start_lat, start_lon = SJSU_LOCATIONS[start_name]
end_lat, end_lon = SJSU_LOCATIONS[end_name]

if "result" not in st.session_state:
    st.session_state.result = None

if st.button("Find Route"):
    try:
        with st.spinner("Calculating route..."):
            graph = load_graph(
                "San Jose State University, San Jose, California, USA",
                network_type=network_type,
            )

            route, distance = shortest_route(
                graph,
                start_lat,
                start_lon,
                end_lat,
                end_lon,
            )

            route_coordinates = get_route_coordinates(graph, route)
            time_minutes = estimate_travel_time(distance, speed_kmh)

            route_map = create_route_map(
                start_lat,
                start_lon,
                end_lat,
                end_lon,
                route_coordinates,
                distance,
            )

            st.session_state.result = {
                "distance": distance,
                "time_minutes": time_minutes,
                "network_type": network_type,
                "route_map": route_map,
            }

    except Exception as error:
        st.error("Something went wrong.")
        st.write(error)

if st.session_state.result:
    result = st.session_state.result

    col1, col2, col3 = st.columns(3)
    col1.metric("Distance", f"{result['distance'] / 1000:.2f} km")
    col2.metric("Estimated Time", f"{result['time_minutes']:.1f} min")
    col3.metric("Mode", result["network_type"])

    st_folium(result["route_map"], width=1100, height=600)
