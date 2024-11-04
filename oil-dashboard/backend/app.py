from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    # Load your analysis data here (e.g., from a CSV or a database)
    data = {
        'prices': [50, 55, 52, 60],  # Example data
        'dates': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
