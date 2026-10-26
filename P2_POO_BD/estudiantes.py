from conexionbd import cursor, conexion

class Estudiantes:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self._nota=nota

    def getNombre(self):
        return self.nombre