## Ejercicio 15: Constructor y Destructor

class Empleado:
    def __init__(self, nombre: str, edad: int):
        """
        Constructor: Permite inicializar instancias de una clase
        """
        self.nombre = nombre
        self.edad = edad
        print(f"¡El empleado llamado {nombre} y de {edad} años ha sido creado!")

    def __del__(self):
        """
        Destructor: Permite eliminar las referencias del objeto
        """
        print(f"El destructor ha sido llamado, el empleado llamado {self.nombre} ha sido eliminado!")

## Ejemplo de prueba / caso de uso

## Creación de dos instancias: llamada al constructor
empleado_1 = Empleado("Martin", 26)
empleado_2 = Empleado("Julien", 24)

## Llamada a los destructores
# Aunque en el código de la imagen se "llama a los destructores",
# la forma estándar de activar el destructor en Python es eliminar
# las referencias al objeto. Usamos 'del' para esto.
del empleado_1
del empleado_2