from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017")

# Seleccionar la base de datos
db = client["mibasededatos"]

# Crear una nueva colección (se crea automáticamente al insertar el primer documento)
coleccion = db["perros"]

# Insertar un solo documento
perro1 = {
    "nombre": "Sando",
    "raza": "doberman",
}
resultado = coleccion.insert_one(perro1)
print(f"Documento insertado con _id: {resultado.inserted_id}")

# Insertar múltiples documentos
perros_nuevos = [
    {"nombre": "Sky", "raza": "pomerania"},
    {"nombre": "Ice", "raza": "husky"}
]
resultado = coleccion.insert_many(perros_nuevos)
print(f"Documentos insertados con _id: {resultado.inserted_ids}")

# Cerrar la conexión
client.close()
