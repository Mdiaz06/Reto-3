class Exams:
    def _init_(self, materia_nombre, lista_preguntas, porcentaje):
        self.materia_nombre = materia_nombre
        self.lista_preguntas = lista_preguntas
        self.porcentaje = porcentaje

lista_Exams = []
lista_materias= ["1.lineal", 
                "2.procesos", 
                "3.apoo"]


def Mostrar ():
    l=0
    while l<len(lista_Exams):
        print(lista_Exams[l].nombre_materia,"- porcentaje", lista_Exams[l].porcentaje, "%")
        for r in lista_Exams[l].lista_preguntas:
            print("pregunta:",r)
        l+=1
def crear_exam():
    materia_nombre=l
    porcentaje=int(input("Ingrese el porcentaje de la evaluación:"))
    numero_preguntas=int(input("Ingrese el numero de preguntas que tendrá la evaluación:"))
    print("Ingrese las preguntas de la evaluación:")
    lista_preguntas=[]
    for n in range(numero_preguntas):
        preguntas= str(input())
        lista_preguntas.append(preguntas)

    exams=Exams(materia_nombre , lista_preguntas, porcentaje)
    lista_Exams.append(exams)
        
    print("Examen guardado:",)
    print("El resultado es:")
    Mostrar()

print("Lista de materias:")
for i in lista_materias:
    print(i)
curso=int(input("Seleccione la materia según su número:"))
if curso==1:
    l="lineal"
    crear_examen()
elif curso==2:
    l="procesos"
    crear_examen()
elif curso==3:
    l="apoo"
    crear_examen()
else:
    while curso < 1 or curso > 5:
        print("Opción incorrecta, por favor ingrese una materia válida")
        curso= int(input("Seleccione una materia:"))
        if curso==1:
            l="lineal"
            crear_examen()
        elif curso==2:
            l="procesos"
            crear_examen()
        elif curso==3:
            l="apoo"
            crear_examen()