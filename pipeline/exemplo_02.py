import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=P4nzgxoiLgk87eKyIO1goek0GBxcggslHhQojJmV"

response = requests.get(url)

print(response.json())
