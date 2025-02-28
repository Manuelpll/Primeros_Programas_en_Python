from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017")

# Seleccionar la base de datos
db = client["mibasededatos"]

# 📌 Crear colección de dueños
coleccion_dueños = db["dueños"]

# Insertar dueños
dueños_nuevos = [
    {"nombre": "Juan", "telefono": "123456789"},
    {"nombre": "María", "telefono": "987654321"},
    {"nombre": "Carlos", "telefono": "555666777"}
]
resultado_dueños = coleccion_dueños.insert_many(dueños_nuevos)
ids_dueños = resultado_dueños.inserted_ids  # Guardamos los _id generados

print(f"Dueños insertados con _id: {ids_dueños}")

# 📌 Crear colección de perros
coleccion_perros = db["perros"]

# Insertar perros con referencias a los dueños
perros_nuevos = [
    {"nombre": "Sando", "raza": "doberman", "dueño_id": ids_dueños[0]},  # Dueño: Juan
    {"nombre": "Sky", "raza": "pomerania", "dueño_id": ids_dueños[1]},   # Dueño: María
    {"nombre": "Ice", "raza": "husky", "dueño_id": ids_dueños[2]}        # Dueño: Carlos
]
resultado_perros = coleccion_perros.insert_many(perros_nuevos)

print(f"Perros insertados con _id: {resultado_perros.inserted_ids}")

# 📌 🔍 Consultar un perro y traer los datos de su dueño usando $lookup (JOIN en MongoDB)
perros_con_dueños = coleccion_perros.aggregate([
    {
        "$lookup": {
            "from": "dueños",        # Nombre de la colección con la que se une
            "localField": "dueño_id",  # Campo en "perros"
            "foreignField": "_id",   # Campo en "dueños"
            "as": "info_dueño"       # Nombre del campo donde se almacenará la info del dueño
        }
    }
])

print("\n📊 Perros con datos de sus dueños:")
for perro in perros_con_dueños:
    print(perro)

# Cerrar la conexión
client.close()
