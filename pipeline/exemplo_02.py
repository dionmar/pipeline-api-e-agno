import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Lê a variável de ambiente
api_key = os.getenv("NASA_API_KEY")

if not api_key:
    print("❌ API_KEY não carregada.")
else:
    print("✅ API_KEY carregada com sucesso.")

# Monta a URL com a chave lida do .env
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={api_key}"

response = requests.get(url)
print(response.json())
