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

# 1️⃣ Actualizar la raza de un perro por su nombre
coleccion.update_one({"nombre": "Sando"}, {"$set": {"raza": "doberman europeo"}})

# 2️⃣ Añadir un nuevo campo "edad" a un perro
coleccion.update_one({"nombre": "Sky"}, {"$set": {"edad": 3}})

# 3️⃣ Incrementar la edad de todos los perros en 1 año
coleccion.update_many({}, {"$inc": {"edad": 1}})

# 4️⃣ Añadir un array de "vacunas" si no existe
coleccion.update_many({}, {"$set": {"vacunas": []}})

# 5️⃣ Añadir una nueva vacuna a los perros de raza "husky"
coleccion.update_many({"raza": "husky"}, {"$push": {"vacunas": "rabia"}})

print("\n📊 Resultados de Aggregations:")

# 1️⃣ Contar cuántos perros hay en la colección
total_perros = coleccion.aggregate([
    {"$count": "total_perros"}
])
print("Total de perros:", list(total_perros))

# 2️⃣ Agrupar por raza y contar cuántos perros hay de cada una
perros_por_raza = coleccion.aggregate([
    {"$group": {"_id": "$raza", "cantidad": {"$sum": 1}}}
])
print("Perros por raza:", list(perros_por_raza))

# 3️⃣ Obtener el perro más joven (mínima edad)
perro_mas_joven = coleccion.aggregate([
    {"$sort": {"edad": 1}},
    {"$limit": 1}
])
print("Perro más joven:", list(perro_mas_joven))

# 4️⃣ Contar cuántos perros tienen vacunas registradas
perros_con_vacunas = coleccion.aggregate([
    {"$match": {"vacunas": {"$exists": True, "$ne": []}}},
    {"$count": "con_vacunas"}
])
print("Perros con vacunas:", list(perros_con_vacunas))

# 5️⃣ Calcular la edad promedio de los perros
edad_promedio = coleccion.aggregate([
    {"$group": {"_id": None, "edad_promedio": {"$avg": "$edad"}}}
])
print("Edad promedio de los perros:", list(edad_promedio))

# Cerrar la conexión
client.close()

