import pandas as pd
import folium
from folium.plugins import MarkerCluster
import html  # for escaping HTML special characters
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Set static folder to serve map HTML files
app.config['STATIC_FOLDER'] = 'static'

# Load the CSV with safe options
df = pd.read_csv("Airbnb_Open_Data.csv", low_memory=False)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Define latitude and longitude column names
latitude_col = "lat"
longitude_col = "long"

# Drop rows with missing location or price
df = df.dropna(subset=[latitude_col, longitude_col, 'price', 'neighbourhood'])

# Clean price column: remove dollar signs and commas, strip any extra spaces, and convert to integer
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).str.strip().astype(int)

@app.route("/", methods=["GET", "POST"])
def index():
    # Filter data based on user input
    neighborhood_filter = request.form.get("neighborhood", "").lower()
    min_price = request.form.get("min_price", 0, type=int)
    max_price = request.form.get("max_price", 2000, type=int)

    df_filtered = df[
        (df['price'] >= min_price) &
        (df['price'] <= max_price)
    ]

    if neighborhood_filter:
        df_filtered = df_filtered[df_filtered['neighbourhood'].str.lower().str.contains(neighborhood_filter)]

    # Initialize folium map
    m = folium.Map(
        location=[df_filtered[latitude_col].mean(), df_filtered[longitude_col].mean()],
        zoom_start=12,
        tiles='CartoDB positron'
    )

    # Add marker cluster
    marker_cluster = MarkerCluster().add_to(m)

    # Add listings to the map
    for _, row in df_filtered.iterrows():
        try:
            # Escape text values to avoid HTML/JS issues
            name = str(row.get('name', 'No name')).replace('"', '').replace('`', '')  # Remove quotes and backticks
            name = html.escape(name)  # Escape special HTML characters
            neighbourhood = html.escape(str(row.get('neighbourhood', 'Unknown')))
            price_display = f"${row['price']}"

            # Build popup content
            popup_content = f"""
                <b>{name}</b><br>
                Price: {price_display}<br>
                Neighborhood: {neighbourhood}
            """
            popup = folium.Popup(popup_content, max_width=250)

            folium.Marker(
                location=[row[latitude_col], row[longitude_col]],
                tooltip=f"{name} ({price_display})",
                popup=popup
            ).add_to(marker_cluster)
        except Exception as e:
            print(f"❌ Failed to render listing with name: {row.get('name', 'No name')}. Error: {e}")

    # Save the map to an HTML file in static folder
    map_html = "airbnb_map_filtered.html"
    map_path = os.path.join(app.config['STATIC_FOLDER'], map_html)
    m.save(map_path)
    print(f"✅ Map saved as {map_path}")

    return render_template("index.html", map_file=map_html)

if __name__ == "__main__":
    app.run(debug=True)
