from pymongo import MongoClient

# URL de conexión (ajústala según tu configuración)
uri = "mongodb://localhost:27017"

# Conectar a MongoDB
client = MongoClient(uri)

# Seleccionar la base de datos
db = client["mibasededatos"]

#Entro a la coleccion amigos
coleccion= db["amigos"]

# Verificar conexión mostrando las colecciones existentes
print("Conectado a la base de datos:", db.name)
print("Colecciones disponibles:", db.list_collection_names())
#Busco todo en la coleccion
documentos = coleccion.find()

#Borrado de Documento
# 1️⃣ Borrar un solo documento (el primero que coincida)
#resultado = coleccion.delete_one({"nombre": "Carlos"})
#Una serie de consultas

# 1️⃣ Obtener todos los documentos
print("\n📌 Todos los documentos:")
for doc in coleccion.find():
    print(doc)

# 2️⃣ Obtener un solo documento (el primero que coincida)
print("\n📌 Primer documento con curso 'DAM2':")
print(coleccion.find_one({"curso": "DAM2"}))

# 3️⃣ Buscar documentos con una condición
print("\n📌 Amigos con nota mayor o igual a 8:")
for doc in coleccion.find({"nota": {"$gte": 8}}):
    print(doc)

# 4️⃣ Filtrar solo algunos campos (excluir el _id)
print("\n📌 Mostrar solo nombres y notas:")
for doc in coleccion.find({}, {"_id": 0, "nombre": 1, "nota": 1}):
    print(doc)

# 5️⃣ Contar documentos con una condición
num_alumnos_dam2 = coleccion.count_documents({"curso": "2DAM"})
print(f"\n📌 Número de alumnos en DAM2: {num_alumnos_dam2}")

# 6️⃣ Ordenar resultados por nota (descendente)
print("\n📌 Amigos ordenados por nota (de mayor a menor):")
for doc in coleccion.find().sort("nota", -1):  # -1 para descendente, 1 para ascendente
    print(doc)

# 7️⃣ Buscar por teléfono (ejemplo de búsqueda exacta)
telefono = "545656885"
print(f"\n📌 Buscar amigo con teléfono {telefono}:")
print(coleccion.find_one({"teléfono": telefono}))

# 8️⃣ Amigos cuyo nombre empieza con "L" (usando expresión regular)
print("\n📌 Amigos cuyo nombre empieza con 'L':")
for doc in coleccion.find({"nombre": {"$regex": "^J"}}):
    print(doc)

client.close()
