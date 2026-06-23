# SmartRoute

SmartRoute is a graph-based route optimization web application built with Python, OSMnx, NetworkX, Folium, and Streamlit.

## Features

- Real OpenStreetMap street data
- Graph-based route optimization
- Shortest path calculation using NetworkX
- Interactive route visualization with Folium
- Streamlit web interface
- Walking, driving, and biking modes
- Travel time estimation
- SJSU landmark dropdown locations

## Technologies Used

- Python
- OSMnx
- NetworkX
- Folium
- Streamlit
- Streamlit-Folium

## How to Run

```bash
git clone https://github.com/andymhuynh/SmartRoute.git
cd SmartRoute
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
