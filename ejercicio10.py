## Corrección del ejercicio 10

## Ejercicio 10: Creación de una clase que contiene varios métodos
class Empleado:
    def __init__(self, nombre: str, funcion: str, salario: float):
        """
        Constructor para inicializar los atributos de la clase:
        nombre ::: str : nombre del empleado
        funcion ::: str : cargo del empleado en la empresa
        salario ::: str : salario del empleado
        """
        self.nombre = nombre
        self.funcion = funcion
        self.salario = salario

        ## Inicialización de la variable horas_trabajadas para contar
        ## las horas trabajadas por el empleado
        self.horas_trabajo = 0

    def trabajar(self, numero_horas: float):
        """
        Este método permite añadir la cantidad de horas realizadas
        a las horas ya trabajadas.
        """
        self.horas_trabajo = self.horas_trabajo + numero_horas
        return f"El empleado {self.nombre} ha trabajado {self.horas_trabajo} horas."

    def info_sueldo(self):
        """
        Este método permite mostrar el salario del empleado.
        """
        return f"El empleado {self.nombre} recibe un salario de {self.salario} euros."

    def dar_aumento(self, cantidad: float):
        """
        Este método permite dar un aumento al empleado
        incrementando su salario actual.
        """
        self.salario = self.salario + cantidad
        return f"El empleado {self.nombre} ha recibido un aumento de {cantidad} euros, lo que le da un salario de {self.salario} euros."
    
    def info_funcion(self):
        """
        Este método permite mostrar el cargo actual del empleado
        """
        return f"El empleado {self.nombre} trabaja como {self.funcion}"


## Ejemplos de pruebas y casos de uso:

# 1. Creación de una instancia
empleado_1 = Empleado("Julien", "Ingeniero", 4000)

## Llamada a métodos

# 2. El empleado trabaja 50 horas
print(empleado_1.trabajar(50))

# 3. Mostrar el sueldo inicial
print(empleado_1.info_sueldo())

# 4. Dar un aumento de 500 euros y mostrar el nuevo sueldo
print(empleado_1.dar_aumento(500))

# 5. Mostrar el cargo del empleado
print(empleado_1.info_funcion())