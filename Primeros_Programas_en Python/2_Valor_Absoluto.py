absoluto = 0
print("Escriba el número separado por un punto")
numero=int(input())
if numero<0: # Compruebo si es positivo o no
    absoluto = -numero
else:
    absoluto= numero
print(f'El valor absoluto de {numero} es {absoluto}')
