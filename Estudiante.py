from Persona import Persona

class Estudiante(Persona): #hereda de la clase Persona
    listaEstudiantes = []
    def __init__(self, nombre, apellido, id, curso):
        super().__init__(nombre, apellido) #utiliza el constructor heredado para asignar los valores
        self.id = id
        self.curso = curso
        self.calificaciones = []
    
    def asignaCalificacion(self, nota):
        self.calificaciones.append(nota)

    #sobrescritura del metodo informacion, para eso tiene que tener el mismo nombre
    def informacion(self):
        super().informacion()
        print("Calificaciones : ")
        print(self.calificaciones)

    #sin sobreescritura
    def informacionEstudiante(self):
        Persona.informacion(self)
        print("Calificaciones : ")
        print(self.calificaciones)

    @classmethod
    def imprimeListaEstudiante (cls):
        for estudiante in cls.listaEstudiantes:
            estudiante.informacion()