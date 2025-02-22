import requests
import json  # Import the JSON module for formatting

# Define API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET Request
response = requests.get(url)

# Validate response status
if response.status_code == 200:
    # Convert response to JSON and print it in a formatted way
    formatted_json = json.dumps(response.json(), indent=4)
    print(formatted_json)
else:
    print(f"Error: {response.status_code}")