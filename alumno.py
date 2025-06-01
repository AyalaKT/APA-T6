class Alumno:
    """
    Clase para gestionar la información académica de un alumno.

    Atributos:
    - numIden:   Número de identificación (entero). Por defecto -1.
    - nombre:    Nombre completo del alumno (cadena).
    - notas:     Lista de notas (números reales).
    """

    def __init__(self, nombre, numIden=-1, notas=None):
        self.numIden = numIden
        self.nombre = nombre
        self.notas = list(notas) if notas else []

    def __add__(self, nota):
        """
        Permite añadir una nota usando '+'. Retorna un nuevo Alumno con la nota añadida.
        Ejemplo: alumno = alumno + 7.5
        """
        return Alumno(self.nombre, self.numIden, self.notas + [nota])

    def media(self):
        """Calcula y devuelve la nota media del alumno."""
        return sum(self.notas) / len(self.notas) if self.notas else 0.0

    def __repr__(self):
        """Devuelve una representación oficial reproducible del objeto Alumno."""
        return f'Alumno("{self.nombre}", {self.numIden}, {self.notas})'

    def __str__(self):
        """Devuelve una representación legible del alumno: ID, nombre y media."""
        return f'{self.numIden}\t{self.nombre}\t{self.media():.1f}'
