from peewee import *

database = MySQLDatabase('hospital', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'Mparr', 'passwd': 'Password_123'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Dept(BaseModel):
    dept_no = IntegerField(column_name='DEPT_NO')
    dnombre = CharField(column_name='DNOMBRE', null=True)
    loc = CharField(column_name='LOC', null=True)

    class Meta:
        table_name = 'dept'
        primary_key = False

class Doctor(BaseModel):
    apellido = CharField(column_name='APELLIDO', null=True)
    doctor_no = IntegerField(column_name='DOCTOR_NO', null=True)
    especialidad = CharField(column_name='ESPECIALIDAD', null=True)
    hospital_cod = IntegerField(column_name='HOSPITAL_COD', null=True)
    salario = IntegerField(column_name='SALARIO', null=True)

    class Meta:
        table_name = 'doctor'
        primary_key = False

class Emp(BaseModel):
    apellido = CharField(column_name='APELLIDO', null=True)
    comision = IntegerField(column_name='COMISION', null=True)
    dept_no = IntegerField(column_name='DEPT_NO', null=True)
    dir = IntegerField(column_name='DIR', null=True)
    emp_no = AutoField(column_name='EMP_NO')
    fecha_alt = DateField(column_name='FECHA_ALT', null=True)
    oficio = CharField(column_name='OFICIO', null=True)
    salario = IntegerField(column_name='SALARIO', null=True)

    class Meta:
        table_name = 'emp'

class Enfermo(BaseModel):
    apellido = CharField(column_name='APELLIDO', null=True)
    direccion = CharField(column_name='DIRECCION', null=True)
    fecha_nac = DateField(column_name='FECHA_NAC', null=True)
    inscripcion = IntegerField(column_name='INSCRIPCION')
    nss = IntegerField(column_name='NSS', null=True)
    sexo = CharField(column_name='SEXO', null=True)

    class Meta:
        table_name = 'enfermo'
        primary_key = False

class Hospital(BaseModel):
    direccion = CharField(column_name='DIRECCION', null=True)
    hospital_cod = IntegerField(column_name='HOSPITAL_COD')
    nombre = CharField(column_name='NOMBRE', null=True)
    num_cama = IntegerField(column_name='NUM_CAMA', null=True)
    telefono = CharField(column_name='TELEFONO', null=True)

    class Meta:
        table_name = 'hospital'
        primary_key = False

class Ocupacion(BaseModel):
    cama = IntegerField(column_name='CAMA', null=True)
    hospital_cod = IntegerField(column_name='HOSPITAL_COD')
    inscripcion = IntegerField(column_name='INSCRIPCION')
    sala_cod = IntegerField(column_name='SALA_COD')

    class Meta:
        table_name = 'ocupacion'
        primary_key = False

class Plantilla(BaseModel):
    apellido = CharField(column_name='APELLIDO', null=True)
    empleado_no = IntegerField(column_name='EMPLEADO_NO')
    funcion = CharField(column_name='FUNCION', null=True)
    hospital_cod = IntegerField(column_name='HOSPITAL_COD', null=True)
    salario = IntegerField(column_name='SALARIO', null=True)
    sala_cod = IntegerField(column_name='SALA_COD', null=True)
    turno = CharField(column_name='TURNO', null=True)

    class Meta:
        table_name = 'plantilla'
        primary_key = False

class Sala(BaseModel):
    hospital_cod = IntegerField(column_name='HOSPITAL_COD')
    nombre = CharField(column_name='NOMBRE', null=True)
    num_cama = IntegerField(column_name='NUM_CAMA', null=True)
    sala_cod = IntegerField(column_name='SALA_COD', null=True)

    class Meta:
        table_name = 'sala'
        primary_key = False

class Users(BaseModel):
    created_date = DateTimeField()
    email = CharField()
    username = CharField(unique=True)

    class Meta:
        table_name = 'users'

