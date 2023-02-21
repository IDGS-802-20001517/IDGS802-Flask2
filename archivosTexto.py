'''
f=open('alumnos.txt','r')
#nombres=f.read()
#print(nombres)

nombres2=f.readlines()
print(nombres2)
f.close()

for items in nombres2:
    print(items,end='')'''

alumno={'Matricula':12345,'Nombre':'Mario','Apellidos':'Lopez','Correo':'mlopez@umanimundila.edu.mx'}
f=open('alumnos.txt','a')
f.write('\n'+'Alejandro')
f.write('\n'+'Saldivar')
f.close()