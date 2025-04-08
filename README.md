# airbnb-geoviz

## Purpose of the Project
The `airbnb-geoviz` project visualizes Airbnb listings on an interactive map. It provides users with a geographical representation of Airbnb data, including details such as price, neighborhood, and descriptions. This project is designed to help users explore Airbnb listings in a user-friendly and visually engaging way.

## Dataset
The project uses a dataset containing Airbnb listings. The dataset includes the following columns:
- **id**: Unique identifier for each listing.
- **name**: Name or title of the listing.
- **price**: Price per night for the listing.
- **neighborhood**: Neighborhood where the listing is located.
- **latitude**: Latitude coordinate of the listing.
- **longitude**: Longitude coordinate of the listing.
- **description**: Additional details about the listing.

> **Note**: The dataset can be downloaded from [AirBnb New York Open Data](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata).

## How the Application Works

### 1. Generating the HTML File (`main.py`)
The `main.py` script processes the dataset and generates an interactive HTML file (`airbnb_map_filtered.html`). Here's how it works:
- **Load Dataset**: The script reads the Airbnb dataset (e.g., CSV or JSON format).
- **Process Data**: It extracts relevant columns and filters listings based on specific criteria (e.g., price range or location).
- **Generate Map**: Using a mapping library like `folium`, the script creates an interactive map. Each listing is represented as a marker on the map, with popups displaying details such as price, neighborhood, and description.
- **Save HTML**: The generated map is saved as an HTML file (`airbnb_map_filtered.html`), which can be opened in any web browser.

### 2. Loading the HTML File (`index.html`)
The `index.html` file is the entry point for viewing the generated map. Here's how it works:
- **Open HTML**: Open the `airbnb_map_filtered.html` file in a web browser.
- **Interactive Map**: The map will display Airbnb listings with markers. Clicking on a marker shows details such as price, neighborhood, and description.

## How to Run the Application

### Prerequisites
- Python 3.x installed on your system.
- Required Python libraries: `pandas`, `folium`, `flask` (install them using `pip`).

### Steps to Run
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd airbnb-geoviz
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate the HTML File**:
   Run the `main.py` script to generate the interactive map:
   ```bash
   python main.py
   ```

4. **View the Map**:
   Open your web browser and navigate to the URL (e.g., `http://127.0.0.1:5000`).

## File Structure
- `main.py`: Script to process the dataset and generate the HTML map.
- `templates/index.html`: Entry file for the UI and map display.
- `static/airbnb_map_filtered.html`: The generated interactive map file.
- `Airbnb_Open_Data.csv`: Dataset containing Airbnb listings.
- `requirements.txt`: List of Python dependencies for the project.

## Future Enhancements
- Add filtering options directly on the map (e.g., by price or neighborhood).
- Optimize runtime for loading a map
