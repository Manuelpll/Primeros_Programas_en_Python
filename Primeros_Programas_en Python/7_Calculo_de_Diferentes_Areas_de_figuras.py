"""Este programa es un programa que te calcula el area de la figura que elijas"""
import math
eleccion =int(input("""Elija la figura que quieres calcular el area:
1. Cuadrado
2. Triangulo
3. Circulo
4. Rombo"""))

def Cuadrado():
    lado=float(input("Ingrese el tamaño de su lado"))
    area=lado*lado
    print(f"El area es{area}")
def Triangulo():
    base=float(input("Ingrese la longitud de la base"))
    altura=float(input("Ingrese la longitud de la altura"))
    area=base*altura
    print(f"El area es {area}")
def Circulo():
    radio=float(input("Ingrese el radio del circulo"))
    numeroPi= math.pi #Para poner el numero Pi se hace de esta forma
    area=math.pi*(radio**2)
    print(f"El area es {area}")
def Rombo():
    diagonalMayor=float(input("Ingrese su diagonal mayor"))
    diagonalMenor=float(input("Ingrese su diagonal menor"))
    area=(diagonalMayor*diagonalMenor)/2
def default():
    print("Opcion no valida")
menu = {
    1:Cuadrado,
    2:Triangulo,
    3:Circulo,
    4:Rombo
}
menu.get(eleccion,default)()