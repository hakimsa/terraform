from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import json
from pymongo import MongoClient


# Configurar el navegador
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Ejecutar sin abrir ventana
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

URL = "https://www.laboutiquedelhogar.es/belleza.html"
driver.get(URL)

# Esperar a que cargue la página
time.sleep(5)

# Buscar productos en la página
productos = []
productos_elements = driver.find_elements(By.CLASS_NAME, "product-items")

for item in productos_elements:
    try:
        nombre = item.find_element(By.CLASS_NAME, "product").text
        precio = item.find_element(By.CLASS_NAME, "price").text
        enlace = item.find_element(By.CLASS_NAME, "product-item-link").get_attribute("href")
        image  = item.find_element(By.CLASS_NAME, "product-image-photo ").get_attribute("src")
        productos.append({"nombre": nombre, "precio": precio, "product-item-link": enlace, "product-image-photo" : image })
    except:
        continue

driver.quit()

# Guardar los datos en JSON
with open("productos.json", "w", encoding="utf-8") as f:
    json.dump(productos, f, indent=4, ensure_ascii=False)

print(f"Se han guardado {len(productos)} productos en productos.json")



def insertar_en_mongo():
    # 🔹 CORRECCIÓN: URI correcta para conectarse a MongoDB Atlas o Local
    MONGO_URI = "mongodb+srv://admin:Cafe2020@cluster0.9pawl.mongodb.net/?retryWrites=true&w=majority"

    try:
        # Conectar a MongoDB
        client = MongoClient(MONGO_URI)
        db = client["peluqueria_db"]  # Nombre de la base de datos
        collection = db["productos"]  # Nombre de la colección
    except Exception as e:
        return f"Error de conexión a MongoDB: {e}"

    # Leer el archivo productos.json
    try:
        with open("productos.json", "r", encoding="utf-8") as file:
            productos = json.load(file)  # Cargar JSON
    except (FileNotFoundError, json.JSONDecodeError):
        return "Error: No se pudo leer productos.json"

    # Verificar si hay datos
    if not productos:
        return "No se encontraron datos"

    # Insertar en MongoDB si hay datos
    collection.insert_many(productos)
    return f"Se insertaron {len(productos)} productos en MongoDB"

# Ejecutar la función y mostrar el resultado
resultado = insertar_en_mongo()
print(resultado)

