from estudiantes import estudiantes

from estudiantes import estudiantes

class App:
    def __init__(self):
        self.main()

    def clear(self):
        print("\033c")

    def pause(self):
        input("... ¡Oprima cualquier tecla para continuar! ...")

    def respuestaSql(self, respuesta):
        if respuesta:
            input("...¡Accion realizada con exito!...")
        else:
            input("...¡No se pudo realizar la accion!...")

    def datosEstudiante(self, tipo):
        estudiantito = {}
        estudiantito['nombre'] = input("Nombre: ").upper().strip()
        estudiantito['nota'] = input("Nota: ").upper().strip()
        return estudiantito

    def menuAcciones(self, tipo):
        print(f"\n\t\t\t...::: Menú de {tipo} :::... \n")
        opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n \t\tSeleccionar Opcion: ").strip()
        return opcion

    def menuEstudiante(self):
        opcion = True
        while opcion:
            self.clear()
            opcion = self.menuAcciones("Estudiantes")
            match opcion:
                case '1':
                    self.clear()
                    estudiantito = self.datosEstudiante("Coche")
                    Estudiante1 = estudiantes.Estudiantes(estudiantito['nombre'], estudiantito['nota'])
                    respuesta = Estudiante1.insertar()
                    self.respuestaSql(respuesta)
                    del Estudiante1
                case '2':
                    self.clear()
                    id = input("ID del estudiante a eliminar: ").strip()
                    respuesta = estudiantes.Estudiantes.eliminar(id)
                    self.respuestaSql(respuesta)
                case '3':
                    id = input("ID del estudiante a actualizar: ").strip()
                    estudiantito = self.datosEstudiante("Coche")
                    Estudiante1 = estudiantes.Estudiantes(estudiantito['nombre'], estudiantito['nota'])
                    respuesta = Estudiante1.actualizar(id)
                    self.respuestaSql(respuesta)
                    del Estudiante1
                case '4':
                    self.clear()
                    registros = estudiantes.Estudiantes.consultar()
                    if len(registros)>0:
                        numEstudiantes = 1
                        for fila in registros:
                            print(f"Estudiante #{numEstudiantes}\nID: {fila[0]}\nNombre: {fila[1]}\nNota: {fila[2]}")
                            numEstudiantes += 1
                            self.pause()
                    else:
                        print("\n\n\t...¡Por el momento no hay datos que mostrar!...")
                case '5':
                    self.clear()
                    opcion = False
                case _:
                    input("...¡Opción invalida!...")


    def main(self):
        opcion = True
        while opcion:
            self.clear()
            print("\n\t\t\t...::: M E N U  P R I N C I P A L :::... \n")
            opcion=input("\n\t 1.- Estudiantes \n\t 2.- Salir \n\t \n\n\t\tSeleccionar Opcion: ").strip()

            match opcion:
                case "1":
                    self.clear()
                    self.menuEstudiante()
                    self.pause()

                case "2":
                    self.clear()
                    print("\n\t...Salir del sistema...")
                    opcion = False
                case _:
                    input("\n\t...¡Opción inválida!...")


if __name__ == "__main__":
    app = App()

