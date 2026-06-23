# SmartRoute

SmartRoute is a graph-based route optimization web application built with Python, OSMnx, NetworkX, Folium, and Streamlit.

The application uses real-world OpenStreetMap data to model roads as weighted graphs and compute shortest routes between locations around San José State University.

---

## Features

- Real OpenStreetMap street data
- Graph-based route optimization
- Shortest path calculation using NetworkX
- Interactive route visualization with Folium
- Streamlit web interface
- Walking, driving, and biking modes
- Travel time estimation
- SJSU landmark dropdown locations

---

## Technologies Used

- Python
- OSMnx
- NetworkX
- Folium
- Streamlit
- Streamlit-Folium

---

## Project Structure

```text
SmartRoute/
├── app.py
├── README.md
├── requirements.txt
├── screenshots/
├── src/
│   ├── routing.py
│   ├── map_viz.py
│   └── utils.py
├── outputs/
└── test_route.py
