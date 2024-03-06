import requests
import json

# Define the URL of your Flask API endpoint
url = "http://localhost:5000"

# Sample input data in JSON format
data = {
    "features": [[1.2, 3.4, 5.6, 2.3]]  # Replace with your actual input data
}

# Send a POST request with the input data to the Flask API
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    result = response.json()
    print("Prediction:", result['prediction'])  # Assuming 'prediction' is the key in the response JSON
else:
    print("Request failed with status code:", response.status_code)
