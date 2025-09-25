## Ejercicio 11: Creación de una clase que contiene varios métodos

class Calculo_Numerico:
    def __init__(self, numero: int):
        self.numero = numero

    def calculo_factorial(self) -> int:
        """
        Este método permite calcular el factorial de un número.
        """
        resultado_fact = 1
        
        ## Por definición, el factorial del número 0 es igual a 1
        if self.numero == 0:
            return 1
        
        ## Almacenamos nuestro número pasado como parámetro en una
        ## variable para no modificar el número inicial
        mi_numero = self.numero
        while mi_numero >= 1:
            ## en cada iteración, multiplicar el número por el resultado
            ## anterior almacenado en la variable resultado_fact
            resultado_fact = resultado_fact * mi_numero
            
            ## decrementar el número pasado como parámetro
            ## en cada iteración por 1
            mi_numero = mi_numero - 1
            
        ## Una vez terminado el cálculo, devolver el resultado
        return resultado_fact

    def lista_divisores(self) -> list:
        """
        Este método permite encontrar la lista de divisores de un número
        """
        resultados_divisores = []
        ## recorrer todos los numeros entre 1 y el "numero" en cuestión, inclusive
        for divisor in range(1, self.numero + 1):
            ## Si el "divisor" que se está revisando es un divisor del "numero" en cuestión,
            ## es decir, que el residuo de la división de numero/divisor es igual a 0
            if self.numero % divisor == 0:
                ## entonces lo añadimos a la lista de divisores
                resultados_divisores.append(divisor)
                
        return resultados_divisores

    def esPrimo(self):
        """
        Este método permite verificar si un número es primo
        """
        lista_dos_divisores = self.lista_divisores()
        ## Un número es primo si tiene dos divisores: 1 y él mismo
        ## Si la lista contiene dos divisores
        if len(lista_dos_divisores) == 2:
            ## entonces el número es primo
            print("El número", self.numero, "es primo")
        else:
            print("El número", self.numero, "no es primo")

    def esPar(self):
        """
        Este método permite verificar si un número es par
        """
        if self.numero % 2 == 0:
            print("El número", self.numero, "es Par")
        else:
            print("El número", self.numero, "es Impar")


## Ejemplos de pruebas y casos de uso:

## Creación de una instancia a partir de
## la clase Calculo_Numerico
primer_calculo = Calculo_Numerico(5)

factorial_5 = primer_calculo.calculo_factorial()
divisores_5 = primer_calculo.lista_divisores()
print("El factorial del número 5 es:", factorial_5)
print("La lista de divisores del número 5 es:", divisores_5)
primer_calculo.esPar()
primer_calculo.esPrimo()
## salto de linea
print()

segundo_calculo = Calculo_Numerico(14)

factorial_14 = segundo_calculo.calculo_factorial()
divisores_14 = segundo_calculo.lista_divisores()
print("El factorial del número 14 es:", factorial_14)
print("La lista de divisores del número 14 es:", divisores_14)
segundo_calculo.esPar()
segundo_calculo.esPrimo()