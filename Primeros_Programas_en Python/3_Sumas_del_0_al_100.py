'''Este programa hace una serie de numeros no decimales con
    sumas desde un numeroro elegido
    a otro sumandole en cada vez un numero indicado'''
indice = float(input("Inserte el numero inicial de la suma:"))
final = float(input("Inserte el numero final de la suma:"))
numeroSumado=float(input("Inserte el numero que quieres que se sume cada vez en la serie:"))
suma = 0
while indice <= final:
    suma = indice
    indice = indice + numeroSumado
    print(int(suma))
print(f'La suma es {int(suma)}')