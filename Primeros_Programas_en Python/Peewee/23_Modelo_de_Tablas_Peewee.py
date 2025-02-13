from datetime import date
from peewee import IntegrityError
from peewee import (
    Model,
    MySQLDatabase,
    IntegerField,
    SmallIntegerField,
    CharField,
    FloatField,
    DateField,
    ForeignKeyField,
    fn,
    JOIN
)
# Conexión a la base de datos MySQL
db = MySQLDatabase(
    'tienda',
    user='Mparr',
    password='Password_123',
    host='localhost',
    port=3306
)

# Clase base para todos los modelos
class BaseModel(Model):
    class Meta:
        database = db

# Tabla: Clientes
class Cliente(BaseModel):
    codigo_cli = SmallIntegerField(primary_key=True)
    nombre = CharField(max_length=20)
    localidad = CharField(max_length=15)
    tlf = CharField(max_length=10, null=True)

# Tabla: Proveedores
class Proveedor(BaseModel):
    codigo_prov = SmallIntegerField(primary_key=True)
    nombre = CharField(max_length=20)
    localidad = CharField(max_length=15)
    fecha_alta = DateField(null=True)
    comision = FloatField()

# Tabla: Artículos
class Articulo(BaseModel):
    codarticulo = SmallIntegerField(primary_key=True)
    denominacion = CharField(max_length=25)
    precio = FloatField()
    stock = SmallIntegerField()
    zona = CharField(max_length=10, null=True)
    codigo_prov = ForeignKeyField(Proveedor, backref='articulos', on_delete='CASCADE', field='codigo_prov')

# Tabla: Compras
class Compra(BaseModel):
    numcompra = SmallIntegerField(primary_key=True)
    codigo_cli = ForeignKeyField(Cliente, backref='compras', on_delete='CASCADE', field='codigo_cli')
    fechacompra = DateField()

# Tabla: DetalleCompras
class DetalleCompra(BaseModel):
    numcompra = ForeignKeyField(Compra, backref='detalles', on_delete='CASCADE', field='numcompra')
    codarticulo = ForeignKeyField(Articulo, backref='detalles', on_delete='CASCADE', field='codarticulo')
    unidades = SmallIntegerField()

    class Meta:
        primary_key = False  # No se usa una clave primaria automática
        indexes = (
            (('numcompra', 'codarticulo'), True),  # Clave primaria compuesta
        )

# Crear las tablas en la base de datos
def crear_tablas():
    with db:
        db.create_tables([Cliente, Proveedor, Articulo, Compra, DetalleCompra])
def insertar_datos():
    try:
        # Insertar 3 clientes
        Cliente.insert_many([
            {'codigo_cli': 1, 'nombre': 'Juan Perez', 'localidad': 'Madrid', 'tlf': '600123456'},
            {'codigo_cli': 2, 'nombre': 'Ana López', 'localidad': 'Barcelona', 'tlf': '601987654'},
            {'codigo_cli': 3, 'nombre': 'Carlos Ruiz', 'localidad': 'Valencia', 'tlf': '602345678'}
        ]).execute()

        # Insertar 3 proveedores
        Proveedor.insert_many([
            {'codigo_prov': 1, 'nombre': 'Proveedor A', 'localidad': 'Sevilla', 'fecha_alta': date(2021, 5, 1), 'comision': 5.5},
            {'codigo_prov': 2, 'nombre': 'Proveedor B', 'localidad': 'Bilbao', 'fecha_alta': date(2022, 3, 15), 'comision': 4.0},
            {'codigo_prov': 3, 'nombre': 'Proveedor C', 'localidad': 'Granada', 'fecha_alta': date(2023, 7, 10), 'comision': 6.0}
        ]).execute()

        # Insertar 3 artículos
        Articulo.insert_many([
            {'codarticulo': 101, 'denominacion': 'Laptop', 'precio': 799.99, 'stock': 10, 'zona': 'A1', 'codigo_prov': 1},
            {'codarticulo': 102, 'denominacion': 'Mouse', 'precio': 19.99, 'stock': 100, 'zona': 'B1', 'codigo_prov': 2},
            {'codarticulo': 103, 'denominacion': 'Teclado', 'precio': 49.99, 'stock': 50, 'zona': 'C1', 'codigo_prov': 3}
        ]).execute()

        # Insertar 3 compras
        Compra.insert_many([
            {'numcompra': 1001, 'codigo_cli': 1, 'fechacompra': date(2024, 11, 15)},
            {'numcompra': 1002, 'codigo_cli': 2, 'fechacompra': date(2024, 11, 16)},
            {'numcompra': 1003, 'codigo_cli': 3, 'fechacompra': date(2024, 11, 17)}
        ]).execute()

        # Insertar 3 detalles de compra
        DetalleCompra.insert_many([
            {'numcompra': 1001, 'codarticulo': 101, 'unidades': 2},
            {'numcompra': 1002, 'codarticulo': 102, 'unidades': 5},
            {'numcompra': 1003, 'codarticulo': 103, 'unidades': 3}
        ]).execute()

        print("Datos insertados correctamente.")

    except IntegrityError as e:
        print("Error al insertar datos:", e)

def consultas():
# 1
    query_clientes = Cliente.select()
    print("--- Clientes ---")
    for cliente in query_clientes:
        print(
            f"ID: {cliente.codigo_cli}, Nombre: {cliente.nombre}, Localidad: {cliente.localidad}, Teléfono: {cliente.tlf}")
    query_compras = Compra.select()

    print("\n--- Compras ---")
    for compra in query_compras:
        print(f"Compra ID: {compra.numcompra}, Cliente: {compra.codigo_cli.nombre}, Fecha: {compra.fechacompra}")

#2
    # print("Query 2:")
    # query_2= (Cliente
    #          .select(
    #              Cliente.codigo_cli,
    #              Cliente.nombre,
    #          Cliente.localidad,
    #              fn.COALESCE(Compra.numcompra, 0).alias('numcompra'),
    #              fn.COALESCE(Compra.fechacompra, '0000-00-00').alias('fechacompra')
    #       )
    #         .join(Compra, JOIN.LEFT_OUTER, on=(Cliente.codigo_cli == Compra.codigo_cli)))
    #
    # for cliente in query_2:
    #  print(f"Cliente ID: {cliente.codigo_cli}, Nombre: {cliente.nombre}, Localidad: {cliente.localidad}, "
    #       f"Compra ID: {cliente.numcompra}, Fecha de compra: {cliente.fechacompra}")

#3
    print("Query 3:")
query_3 = (DetalleCompra
         .select(
             Cliente.codigo_cli,
             Cliente.nombre,
             Cliente.localidad,
             Compra.numcompra,
             Articulo.codarticulo,
             DetalleCompra.unidades,
             Articulo.precio,
             (DetalleCompra.unidades * Articulo.precio).alias('importe')
         )
         .join(Compra, on=(DetalleCompra.numcompra == Compra.numcompra))
         .join(Cliente, on=(Compra.codigo_cli == Cliente.codigo_cli))
         .join(Articulo, on=(DetalleCompra.codarticulo == Articulo.codarticulo)))

for detalle in query_3:
    print(f"Cliente ID: {detalle.cliente.codigo_cli}, Nombre: {detalle.cliente.nombre}, "
          f"Compra ID: {detalle.numcompra}, Artículo: {detalle.articulo.codarticulo}, "
          f"Unidades: {detalle.unidades}, Precio: {detalle.articulo.precio}, "
          f"Importe: {detalle.importe}")

#4
    # print("Query 4:")
    # query_4 = (Compra
    #          .select(
    #     Cliente.codigo_cli,
    #     Cliente.nombre,
    #     Cliente.localidad,
    #     Compra.numcompra,
    #     fn.SUM(DetalleCompra.unidades * Articulo.precio).alias('total_compra')
    # )
    #          .join(DetalleCompra, on=(Compra.numcompra == DetalleCompra.numcompra))
    #          .join(Articulo, on=(DetalleCompra.codarticulo == Articulo.codarticulo))
    #          .join(Cliente, on=(Compra.codigo_cli == Cliente.codigo_cli))
    #          .group_by(Cliente.codigo_cli, Compra.numcompra))
    #
    # for compra in query_4:
    #     print(f"Cliente ID: {compra.cliente.codigo_cli}, Nombre: {compra.cliente.nombre}, "
    #           f"Compra ID: {compra.numcompra}, Total de compra: {compra.total_compra}")

#5
    # print("Query 5:")
    # query_5 = (Cliente
    #          .select(
    #     Cliente.codigo_cli,
    #     Cliente.nombre,
    #     Cliente.localidad,
    #     Cliente.tlf,
    #     fn.COUNT(Compra.numcompra).alias('num_compras'),
    #     fn.SUM(DetalleCompra.unidades * Articulo.precio).alias('total_importe')
    # )
    #          .join(Compra, JOIN.LEFT_OUTER, on=(Cliente.codigo_cli == Compra.codigo_cli))
    #          .join(DetalleCompra, JOIN.LEFT_OUTER, on=(Compra.numcompra == DetalleCompra.numcompra))
    #          .join(Articulo, JOIN.LEFT_OUTER, on=(DetalleCompra.codarticulo == Articulo.codarticulo))
    #          .group_by(Cliente.codigo_cli))
    #
    # for cliente in query_5:
    #     print(f"Cliente ID: {cliente.codigo_cli}, Nombre: {cliente.nombre}, Localidad: {cliente.localidad}, "
    #           f"Número de Compras: {cliente.num_compras}, Total de compras: {cliente.total_importe}")

if __name__ == "__main__":
    consultas()

