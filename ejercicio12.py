## Ejercicio 12: Herencia múltiple

class Video:
    def __init__(self, titulo: str, categoria: str, duracion: int):
        """
        Inicialización de los atributos de la clase
        """
        ## Título del video
        self.titulo = titulo
        ## duración en minutos
        self.duracion = duracion
        ## Categoria del video
        self.categoria = categoria

    def mirar_video(self):
        """
        Este método permite ver el video:
        Muestra en la consola la información relacionada con el video
        """
        print("Iniciando el video...")
        print(f"El video que estás viendo se titula '{self.titulo}' " +
              f"de la categoría '{self.categoria}' con una duración de {self.duracion} minutos.")

    def detener_video(self):
        """
        Este método permite detener el video
        """
        print("Deteniendo el video.")

class Audio:
    def __init__(self, nombre_artista: str, titulo: str):
        """
        Inicialización de los atributos
        """
        ## Título del audio
        self.titulo = titulo
        ## Nombre del artista
        self.nombre_artista = nombre_artista

    def escuchar_audio(self):
        """
        Este método permite escuchar el audio mostrando una cadena de caracteres en la consola y
        muestra la información relacionada con el audio
        """
        print("Iniciando el audio... ")
        print(f"El audio que estás escuchando es '{self.titulo}' producido \n"
              f"por el artista '{self.nombre_artista}'")

    def detener_audio(self):
        """
        Detener la reproducción del audio
        """
        print("Deteniendo la reproducción del audio.")


class Media(Video, Audio):
    """
    Herencia múltiple: Esta clase hereda de la clase Video y de la clase Audio al mismo tiempo
    """
    def __init__(self, titulo: str, categoria: str, duracion: int, nombre_artista: str):
        
        # Inicialización de los atributos de Video
        Video.__init__(self, titulo, categoria, duracion)
        
        # Inicialización de los atributos de Audio (Título se pasa como argumento)
        Audio.__init__(self, nombre_artista, titulo)


## Ejemplos de pruebas / casos de uso

## creación de una instancia
media_1 = Media("Título 1", "infantil", 100, "Artista 1")

## escuchar el audio
media_1.escuchar_audio()

## ver el video
media_1.mirar_video()

## detener el audio
media_1.detener_audio()

## detener el video
media_1.detener_video()