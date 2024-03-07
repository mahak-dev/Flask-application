import requests
import json

url = "http://localhost:5000"

# Sample input data in JSON format
data = {
    "features": [[1.2, 3.4, 5.6, 2.3]]
}

# Send a POST request with the input data to the Flask API
response = requests.post(url, json=data)


if response.status_code == 200:
    
    result = response.json()
    print("Prediction:", result['prediction'])  # Assuming 'prediction' is the key in the response JSON
else:
    print("Request failed with status code:", response.status_code)
