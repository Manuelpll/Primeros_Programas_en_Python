class Persona():
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

        # Creación de un nuevo método

    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}")
        print(presentacion.format(self.nombre, self.edad, self.ocupacion))



    def contratar(self, puesto):
        self.puesto = puesto
        print("{} ha sido contratado como {}".format(self.nombre, self.puesto))
        self.ocupacion = puesto


Borja = Persona(21, "Borja", "Desocupado")
Borja.presentar()
Borja.contratar("Butanero")
Borja.presentar()