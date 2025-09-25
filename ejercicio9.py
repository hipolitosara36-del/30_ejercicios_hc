## Ejercicio 9: Herencia - Creación de una clase padre y una clase hijo

## Creación de la clase Padre
class Vehiculo:
    def __init__(self, marca: str, velocidad_i: float = 0):
        """
        Constructor para inicializar los atributos:
        marca ::: str : la marca del coche
        velocidad_i ::: float : la velocidad inicial del coche
        >>> velocidad_i tiene un valor predeterminado = 0
        """
        self.marca = marca
        self.velocidad = velocidad_i

    def acelerar(self, v: float):
        """
        Este método permite aumentar la velocidad del coche.
        """
        self.velocidad += v

    def desacelerar(self, v: float):
        """
        Este método permite disminuir la velocidad del coche.
        """
        self.velocidad -= v

    def mostrar_velocidad(self):
        """
        Este método permite mostrar la velocidad actual del coche.
        """
        print(f"Tu velocidad actual es: {self.velocidad} km/h")

## Constructor para inicializar los atributos de la clase hija
class Coche(Vehiculo):
    def __init__(self, marca: str, velocidad_i: float = 0, bocina: str = "tuuut !"):
        """
        Constructor para inicializar los atributos de la clase hija
        """
        ## Inicialización de los atributos heredados de la Clase Padre.
        super().__init__(marca, velocidad_i)
        
        ## Atributo adicional específico de la Clase Hijo
        self.bocina = bocina

    def tocar_claxon(self):
        """
        Este método permite tocar la bocina, devolviendo una cadena de caracteres.
        """
        print(self.bocina)

#---------------------------------------------------------
## Ejemplos de pruebas y casos de uso:

## Creación de una instancia coche_1.
# El segundo argumento (10.5) se asigna a velocidad_i
coche_1 = Coche("Peugeot 208", 10.5)

## Mostrar la velocidad inicial del coche mostrando
## el atributo de la instancia coche_1.
print("La velocidad inicial del coche es:", coche_1.velocidad, "km/h")

## Llamada a métodos

## Aumento de la Velocidad en 50km/h
coche_1.acelerar(50)

## Disminución de la velocidad en 15km/h
coche_1.desacelerar(15)

## Mostrar la Velocidad actual del coche
coche_1.mostrar_velocidad()

## Tocar la bocina
coche_1.tocar_claxon()
