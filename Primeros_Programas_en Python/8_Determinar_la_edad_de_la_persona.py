""" Este programa determina la edad del usuario"""
while True:
    edad = int(input("""Para salir pulse 0
    Introduce la edad que tienes: """))
    if 3 > edad > 0:
        print("Eres un bebe")
    elif 3 < edad < 18:
        print("Eres un joven")
    elif 18 <= edad < 67:
        print("Eres adulto")
    elif edad > 67:
        print("Eres pensionista")
    elif edad == 0:
        print("Saliendo del programa...")
        break
    else: print("No es posible")