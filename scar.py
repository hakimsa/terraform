import requests
from bs4 import BeautifulSoup
import json

# URL de la página de productos de peluquería
URL = "https://www.productosdelapeluqueria.es/5-peluqueria"

# Encabezados para simular un navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Hacer la solicitud HTTP
response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrar todos los productos en la página
    productos = []
    for item in soup.find_all("div", class_="product row"):
        nombre = item.find("a", class_="products").text.strip()
        precio = item.find("span", class_="price").text.strip() if item.find("span", class_="price") else "No disponible"
        enlace = item.find("a", class_="products")["href"]

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "enlace": enlace
        } 
    # Guardar la información en un archivo JSON
    with open("productos.json", "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)

    print(f"Se han guardado {len(productos)} productos en productos.json")

e
