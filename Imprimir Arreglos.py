print("Programa de arreglos")
Nombres=[]
respuesta=0
emp=0
while respuesta!=4:
	respuesta=0
	print("Bienvenido al programa de empleados python :3")
	print("Escribe las siguientes opciones a realizar: ")
	print("Para añadir empleados ingrese 1")
	print("Para eliminar empleados ingrese 2")
	print("Para imprimir empleados ingrese 3")
	print("Para salir ingrese 4")
	respuesta=int(input())
	if respuesta==1:
		nombre=input("Nombre:")
		Nombres.append(nombre)
		print("Empleado Registrado")
		emp+1
	elif respuesta==3:
		print("Lista de empleados:")
		for i in Nombres:
			print(i)
		
