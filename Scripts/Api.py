from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load or create dummy data for demonstration
def load_brent_oil_data():
    # Example of a DataFrame with dates, prices, and event info
    events = [
        "None", 
        "Political Decision", 
        "Conflict in Oil-Producing Region", 
        "Global Economic Sanction", 
        "Change in OPEC Policy"
    ]
    
    # Generate dummy data with a mix of events
    data = pd.DataFrame({
        "date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
        "price": np.random.normal(loc=70, scale=10, size=100),
        "event": [np.random.choice(events) for _ in range(100)]
    })
    return data

# Route for getting historical oil price data
@app.route("/api/oil_prices", methods=["GET"])
def get_oil_prices():
    data = load_brent_oil_data()
    
    # Get query parameters for filtering
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    
    # Filter data if date range is specified
    if start_date and end_date:
        data = data[(data["date"] >= start_date) & (data["date"] <= end_date)]
    
    result = data.to_dict(orient="records")
    return jsonify(result)

# Route for getting specific data based on event filter
@app.route("/api/oil_prices_by_event", methods=["GET"])
def get_oil_prices_by_event():
    data = load_brent_oil_data()
    event_type = request.args.get("event", "None")  # Default to "None" if no event is specified
    
    # Filter based on event
    filtered_data = data[data["event"] == event_type]
    result = filtered_data.to_dict(orient="records")
    return jsonify(result)

# Route for getting analysis metrics (e.g., RMSE, MAE)
@app.route("/api/metrics", methods=["GET"])
def get_metrics():
    metrics = {
        "RMSE": round(np.random.uniform(0.5, 1.5), 2),
        "MAE": round(np.random.uniform(0.3, 1.0), 2),
        "Volatility": round(np.std(np.random.normal(loc=70, scale=10, size=100)), 2)
    }
    return jsonify(metrics)

# Route for getting summary statistics of the dataset
@app.route("/api/summary_statistics", methods=["GET"])
def get_summary_statistics():
    data = load_brent_oil_data()
    summary_stats = data.describe().to_dict()
    return jsonify(summary_stats)

# Optional: Route for real-time updates (dummy implementation)
@app.route("/api/real_time_update", methods=["GET"])
def get_real_time_update():
    latest_data = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "price": round(np.random.normal(loc=70, scale=10), 2),
        "event": "None"
    }
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(debug=True)
