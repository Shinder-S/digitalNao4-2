import requests
from bs4 import BeautifulSoup

url = "https://resultados.lapaginamillonaria.com/futbol/liga-profesional-lpa-arg/clasificacion/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

equipos = soup.select(".table-row")  # Selector CSS para las filas de la tabla de equipos y puntos

resultados = []

for equipo in equipos:
    nombre_equipo = equipo.select_one(".team-name").text
    puntos = equipo.select_one(".team-points").text

    resultado_equipo = {
        "Equipo": nombre_equipo,
        "Puntos": puntos
    }

    resultados.append(resultado_equipo)

# Imprimir los resultados
for resultado in resultados:
    print(f"Equipo: {resultado['Equipo']}")
    print(f"Puntos: {resultado['Puntos']}")
    print()