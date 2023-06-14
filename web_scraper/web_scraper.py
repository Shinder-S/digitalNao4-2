import requests
from bs4 import BeautifulSoup

#Acá definimos la página que vamos a "raspar"
url = "https://lapaginamillonaria.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Imprimir los resultados
titulares = soup.find_all("a")
for titular in titulares:
    print(titular.get("href")) 