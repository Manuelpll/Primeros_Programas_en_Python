peso= 0.5 # medido en gramos
pesoR= 1# medido en kilogramos
precioT= 0
dineroEntregado = 0.0
dineroDevuelta= 0.0
print("Escriba el codigo de la fruta que deseas")
codigo=input()
if(codigo=="1"):
    precioT= pesoR*1.3
    print(f'El precio de la naranja es {precioT}')
    print("Introduzca el dinero con el que quieres pagar")
    dineroEntregado= float(input())
    dineroDevuelta= dineroEntregado-precioT
    print(f'La vuelta es de {dineroDevuelta}')
elif(codigo=="2"):
    precioT= pesoR*1.6
    print(f'El precio de la mandarina es {precioT}')
    print("Introduzca el dinero con el que quieres pagar")
    dineroEntregado = float(input())
    dineroDevuelta = dineroEntregado - precioT
    print(f'La vuelta es de {dineroDevuelta}')
elif(codigo=="3"):
    precioT= pesoR*0.6
    print(f'El precio de ciruelas es {precioT}')
    print("Introduzca el dinero con el que quieres pagar")
    dineroEntregado = float(input())
    dineroDevuelta = dineroEntregado - precioT
    print(f'La vuelta es de {dineroDevuelta}')
else:print("No hay ningun producto asignado a este codigo")