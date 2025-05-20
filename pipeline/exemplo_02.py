import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=NASA_API_KEY"

response = requests.get(url)

print(response.json())
