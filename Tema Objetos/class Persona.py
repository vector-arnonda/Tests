import re
class Alumno:
    def __init__(self,nombre,instituto,clase,edad,estatura,dni,gafas):
        self.nombre=nombre
        self.instituto=instituto
        self.clase=clase
        self.edad=edad
        self.estatura=estatura
        self.dni=dni
        self.gafas=gafas
    
    def __repr__(self):
        return f'Persona({self.nombre},{self.edad},{self.dni})'         
    
    def medad(self,a):
        if self.edad>=18:
            print(f"{a} es mayor de edad")
        else:
            print(f"{a} no es mayor de edad")
    
    def checkdata(self):
        if not isinstance(self.nombre, str) and len(self.nombre) > 2:
            self.nombre=input("El nombre solo puede contener letras, introduzcalo de nuevo: ")
        if not isinstance(self.edad,int) and self.edad>0:
            self.edad=input("La edad no puede contener letras y debe de ser mayor a 0, introduzcala de nuevo: ")
        if not re.match(r'\d{8}[a-zA-Z]$', self.dni):
            self.dni=input("DNI incorrecto, escribalo de nuevo: ")
    
    def order(personas):
        porder=sorted(personas, key=lambda x: x[1])

persona1=Alumno("Alex","IES Camp de Morvedre","B1A")
persona2=Alumno("Jorge","IES Camp de Morvedre","B1A")
persona3=Alumno("Eustaquio","IES Maria Moliner","B2B")
persona4=Alumno("Juan","IES Maria Moliner","B2B")
persona5=Alumno("Jose","IES Jorge Juan","CS1A")
persona6=Alumno("Ian","IES Jorge Juan","CS1B")

alumnos=[]

for i in range(1,7):
    personas.append(globals()["persona{}".format(i)])



