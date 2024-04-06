#Este codigo te imprime la posicion de la serie fibonacci que deseas
def fibonacci(n):
    if n <= 0:
        return "Por favor ingresa un número entero positivo"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[-1]

# Solicitar al usuario que ingrese el número deseado de la serie Fibonacci
posicion_deseada = int(input("Ingresa el número deseado de la serie Fibonacci: "))
#Imprime la posicion deseada y el numero que sale
print(f"El número en la posición {posicion_deseada} de la serie Fibonacci es: {fibonacci(posicion_deseada)}")