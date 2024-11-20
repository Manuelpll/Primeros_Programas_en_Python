from datetime import date
import mysql.connector as bd

bd_conexion = bd.connect(host='localhost', port='3306',
                                   user='root', password='Password_123', database='hospital')


cursor = bd_conexion.cursor()


ConsultaAlta = ("INSERT INTO emp "
               "(emp_no,apellido,oficio,dir,fecha_alt,salario, comision,dept_no) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")


datosEmpleados = (2290,'Benito', 'Programador',7566,  date(1976, 6, 4),100000,100,20)


cursor.execute(ConsultaAlta, datosEmpleados)

bd_conexion.commit()

datosEmpleados = (2291,'Ana', 'Diseñadora',7567,  date(1990, 8, 9),100200,120,20)

cursor.execute(ConsultaAlta, datosEmpleados)

bd_conexion.commit()

cursor.close()
bd_conexion.close()