"""Este es un programa que te permite calcular las posiciones de tres numeros enteros"""

numero1 = int(input("Introduce un primer numero: "))
numero2 = int(input("Introduce un segundo numero: "))
numero3 = int(input("Introduce un tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f'El numero mayor es {numero1}')
elif numero2 > numero1 and numero2 >numero3:
    print(f'El numero mayor es {numero2}')
else: print(f'El numero mayor es {numero3}')

if numero1 > numero2 and numero1 < numero3:
    print(f'El numero intermedio es {numero1}')
elif numero2 < numero3:
    print(f'El numero intermedio es {numero2}')
else: print(f'El numero intermedio es {numero3}')

if  numero1 < numero2 and numero1 < numero3:
    print(f'El numero menor es {numero1}')
elif numero2 < numero1 and numero2 < numero3:
    print(f'El numero menor es {numero2}')
else: print(f'El numero menor es {numero3}')