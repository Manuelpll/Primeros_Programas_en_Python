import datetime
import peewee

# Conexión a la base de datos MySQL
database = peewee.MySQLDatabase('hospital', user='Mparr', password='Password_123', host='localhost', port=3306)

# Definición del modelo User
class User(peewee.Model):
    username = peewee.CharField(unique=True)  # Asegúrate de solo usar unique=True
    email = peewee.CharField(index=True)  # Elimina 'index=True' si ya no lo necesitas
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = "Users"

# Creación de la tabla si no existe
if __name__ == '__main__':
    database.connect()  # Conectar a la base de datos

    if not User.table_exists():
        User.create_table()

    # Solicitar datos al usuario
    username = input("Ingrese un nombre: ")
    email = input("Ingrese un birthday: ")

    # Verificar si el usuario ya existe
    if not User.select().where(User.username == username).exists():
        new_user = User.create(username=username, email=email)
        print(f"Usuario '{new_user.username}' se ha registrado correctamente.")
    else:
        print("El usuario ya se encuentra registrado.")

    database.close()  # Cerrar la conexión a la base de datos
