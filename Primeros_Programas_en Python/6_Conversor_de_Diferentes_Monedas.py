"""Este programa es un programa que te permite calcular las conversiones de moneda de diferentes paises (En un futuro puede que se añadan más)"""
cantidadDeMonedas = float(input("Ingrese la cantidad quiere convertir (Si quieres poner decimales en vez de , pon .) : "))
cantidadDeMonedas = round(cantidadDeMonedas,2)
cantidadResultante = 0
eleccion =int(input("""Seleciona de que moneda a que moneda quieres convertirla:
 1: De euros a Libra Esterlina (Inglaterra)
 2: De euros a  yenes (Japon)
 3: De euros a Bats (Tailandia)
 4: De euros a dolares (EEUU)
 5: De euros a  Corona Islandesa (Islandia)
 """))

def EuroLibraEsterlina():
    cantidadResultante = cantidadDeMonedas / 1.17
    cantidadResultante = round(cantidadResultante, 2)
    print(f'La cantidad de Libras Esterlinas que tienes con {cantidadDeMonedas} euros son {cantidadResultante} £')
def EurosYenes ():
    cantidadResultante = cantidadDeMonedas / 0.0061
    cantidadResultante = round(cantidadResultante, 2)
    print(f'La cantidad de Yenes que tienes con {cantidadDeMonedas} euros son {cantidadResultante} ¥')

def EurosBats ():
    cantidadResultante = cantidadDeMonedas / 0.026
    cantidadResultante = round(cantidadResultante, 2)
    print(f'La cantidad de Yenes que tienes con {cantidadDeMonedas} euros son {cantidadResultante} ฿')

def EurosDolares ():
    cantidadResultante = cantidadDeMonedas / 0.92
    cantidadResultante = round(cantidadResultante, 2)
    print(f'La cantidad de Yenes que tienes con {cantidadDeMonedas} euros son {cantidadResultante} $')
def EuroCoronaIslandesa ():
    cantidadResultante = cantidadDeMonedas / 0.0067
    cantidadResultante = round(cantidadResultante, 2)
    print(f'La cantidad de Yenes que tienes con {cantidadDeMonedas} euros son {cantidadResultante} ISK')
def default():
    print("Opción no existente")
menu = {
    1: EuroLibraEsterlina,
    2: EurosYenes,
    3: EurosBats,
    4: EurosDolares,
    5: EuroCoronaIslandesa
}#Claves para llamar a los metodos
menu.get(eleccion,default)()