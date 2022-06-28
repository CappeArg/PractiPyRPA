class Humano:
    def __init__(self, edad):
        self.edad = edad
        print("soy un nuevo objeto")

    def hablar(self,mensaje):
        print(mensaje)

class IngSistemas(Humano):
    def programar(self,lenguaje):
        print('voy a programar en ', lenguaje)

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print('Debo estudiar el caso de ', de)

pedro = IngSistemas(26)

raul = LicDerecho(21)

print('Soy Pedro y tengo ',pedro.edad)
print('Soy Raul y tengo ',raul.edad)

pedro.programar('Python')

raul.estudiarCaso('Pedro')

pedro.hablar('Hola')

raul.hablar('Hola, Pedro!')
