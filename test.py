import requests

# Define the URL of the Flask API
url = 'https://trail-app-593028519055.us-central1.run.app/predict'

# Define the feature values (from the provided list)
data = {
    'features': [ 1, 39, 4.0, 0, 0.0, 0.0, 0, 0, 0, 195.0, 106.0, 70.0, 26.97, 80.0, 77.0]
}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Print the raw response to debug
print("Response status code:", response.status_code)
print("Raw response text:", response.text)

# Try to print the JSON response
try:
    json_response = response.json()
    print(f"Prediction: {json_response['prediction']}")
except requests.exceptions.JSONDecodeError:
    print("Error decoding JSON response. Response content:", response.text)
