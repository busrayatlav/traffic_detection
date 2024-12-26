
# Traffic Detection and Optimization Project

This repository contains a comprehensive traffic detection and optimization project for Berlin. It integrates traffic, weather, public transportation, and construction data to build predictive models and optimize routes.

## Data Sources

- **Traffic Data**:
  - **Source**: Berlin Municipality Traffic Management Division.
  - **Access**: Berlin's official website provides traffic flow and congestion data. The Traffic Detection Berlin API is also utilized.
  - **Dataset**: [Traffic Detection API](https://api.viz.berlin.de/daten/verkehrsdetektion)

- **Weather Data**:
  - **Sources**:
    - [Open-Meteo](https://open-meteo.com/en/docs/dwd-api#latitude=52.5244&longitude=13.4105): High-resolution free weather data.
    - [WeatherAPI.com](https://www.weatherapi.com/): Real-time and historical weather data.
    - [OpenWeatherMap](https://openweathermap.org/): Provides diverse weather APIs.
  - **Dataset**: Open-Meteo JSON API.

- **Public Transport Data**:
  - **Source**: Berliner Verkehrsbetriebe (BVG).
  - **Access**: Developer portal and Trafi platform for integrated public transportation schedules and routes.
  - **Dataset**: [BVG GTFS Data](https://daten.berlin.de/datensaetze/vbb-fahrplandaten-via-gtfs)

- **Road and Construction Information**:
  - **Source**: Berlin Municipality's announcements on roadworks and construction projects.
  - **Access**: Official website provides updates on roadworks and restrictions.
  - **Dataset**: [Roadwork Data API](https://api.viz.berlin.de/daten/verkehrsdetektion)

## Code Overview

### Installing Required Libraries
To set up the environment, install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Key Modules
- **`data_processing.py`**: Functions to load, clean, and preprocess datasets.
- **`modeling.py`**: Machine learning models for traffic prediction.
- **`visualization.py`**: Visualization tools for spatial and temporal traffic patterns.

### Highlights
- **Predictive Modeling**:
  - Linear Regression
  - Random Forest
  - K-Means Clustering
  - Gradient Boosting (XGBoost, CatBoost)
  - Neural Networks

- **Route Optimization**:
  - Integrates OpenRouteService API for route calculations and optimizations.
  - Visualizes road networks and routes using OSMnx.

- **Data Integration**:
  - Combines traffic, weather, construction, and public transportation data.
  - Enhances features with additional metrics like holiday indicators and weekend information.

## Visualization Examples

### Traffic Clustering
Using K-Means clustering to identify traffic patterns.

![image](https://github.com/user-attachments/assets/b90276d5-a18a-4553-bc71-099ef5a8cc48)

### Road Network Visualization
Berlin road network with optimized routes.
<img src="https://github.com/user-attachments/assets/558dfbaa-c37b-4eb1-b7bb-93384c18f3fb" alt="Image Description" width="50">

### Model Comparison
Performance comparison of models based on MSE and R² scores.

![image](https://github.com/user-attachments/assets/2b228255-8b8a-4db1-a7e7-f139e7e598cb)
![image](https://github.com/user-attachments/assets/9edf40c5-1482-4546-8940-94366dde6db7)

## How to Use
1. Clone this repository:
```bash
git clone https://github.com/busrayatlav/traffic_detection.git
```
2. Navigate to the project directory:
```bash
cd traffic_detection
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Streamlit app locally:
```bash
streamlit run app.py
```

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the Berlin Municipality and data providers like Open-Meteo, BVG, and OpenRouteService for making this project possible.
