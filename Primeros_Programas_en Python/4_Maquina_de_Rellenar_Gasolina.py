"""Este programa es una maquina de gasolina dependiendo de la gasolina que pidas te cobrara de una forma diferente"""
litros = int(input("Cuanos litros de gasolina quieres: "))
elecion = int(input("""Que tipo quieres:
1. Diesel
2. Super92
3. Sin_Plomo_95
"""))
def Diesel():
   precio=litros*1.6
   print(f'El precio de la Diesel es {precio}')
   print("Introduzca el dinero con el que quieres pagar")
   dineroEntregado = float(input())
   dineroDevuelta = dineroEntregado - precio
   dineroDevuelta = round(dineroDevuelta, 2)#Redondea a 2 decimales
   print(f'La vuelta es de {dineroDevuelta}')
#Metodo para el tipo Diesel
def Super92():
    precio = litros * 1.7
    print(f'El precio de la Super92 es {precio}')
    print("Introduzca el dinero con el que quieres pagar")
    dineroEntregado = float(input())
    dineroDevuelta = dineroEntregado - precio
    dineroDevuelta = round(dineroDevuelta, 2)
    print(f'La vuelta es de {dineroDevuelta}')
#Metodo para el tipo Super92
def Sin_Plomo_95():
    precio = litros * 1.645
    print(f'El precio de la Sin_Plomo_95 es {precio}')
    print("Introduzca el dinero con el que quieres pagar")
    dineroEntregado = float(input())
    dineroDevuelta = dineroEntregado - precio
    dineroDevuelta = round(dineroDevuelta, 2)
    print(f'La vuelta es de {dineroDevuelta}')
#Metodo para el tipo Sin_Plomo_95
def default():
    print("Opción no valida")

menu = {
    1: Diesel,
    2: Super92,
    3: Sin_Plomo_95
}#Claves para llamar a los metodos

menu.get(elecion, default)()
