from Persona import Persona
from Estudiante import Estudiante

alex = Estudiante("Alex","Martinez",12345,"Fundamentos")

alex.asignaCalificacion(8.9)
alex.informacion()
alex.informacionEstudiante()

nombre = input("Proporciona tu nombre:")

print(f"Bienvenido {nombre}")

print("***** MENU *****")
print("1. Agregar una persona")
print("2. Mostrar lista de personas")
print("3. Agregar un estudiante")
print("4. Mostrar lista de estudiantes")
print("3. Terminar el programa")

opcion = input("Opcion a elegir: ")

while (opcion != "5"):
    if opcion == "1":
        Nombre = input("Dame el nombre de la persona: ")
        Apellido = input("Dame el apellido de la persona: ")
        nuevaPersona = Persona(Nombre, Apellido)
    elif opcion == "2":
        print("Mostrando la lista de personas")
        Persona.imprimeListaPersona()
    elif opcion == "3":
        Nombre = input("Dame el nombre del estudiante: ")
        Apellido = input("Dame el apellido del estudiante: ")
        id = input("Dame el ID del estudiante: ")
        curso = input("Dame el curso del estudiante: ")
        id = Estudiante(Nombre, Apellido, int(id), curso)
    elif opcion == "4":
        print("Lista de estudiantes")
        Estudiante.imprimeListaEstudiante()
    else:
        print("Opcion incorrecta")
    
    print("***** MENU *****")
    print("1. Agregar una persona")
    print("2. Mostrar lista de personas")
    print("3. Agregar un estudiante")
    print("4. Mostrar lista de estudiantes")
    print("3. Terminar el programa")

    opcion = input("Opcion a elegir: ")