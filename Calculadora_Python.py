print("Calculadora de Python version 1.0")

def suma():
	print("Escribe el primer numero")
	s1=int(input())
	print("Escribe el segundo numero")
	s2=int(input())
	suma=s1+s2
	print("El resultado de la suma es:", suma)

def resta():
	print("Escribe el primer numero")
	r1=int(input())
	print("Escribe el segundo numero")
	r2=int(input())
	resta=r1-r2
	print("El resultado de la suma es:", resta)

def div():
	print("Escribe el primer numero")
	d1=float(input())
	print("Escribe el segundo numero")
	d2=float(input())
	div=d1/d2
	print("El resultado de la suma es:", div)
n1=0
repeat=1
while n1!=4:
	n1=0
	repeat=1
	print("Seleccione la opcion que desea realizar:")
	print("1 para la suma")
	print("2 para la resta")
	print("3 para division")
	print("4 para salir")
	n1=int(input())

	if n1==1:
		while repeat!=0:
			suma()
			print("Escribe 0 para volver al menu o cualquier otro numero para continuar")
			repeat=int(input())
	elif n1==2:
		while repeat!=0:
			resta()
			print("Escribe 0 para volver al menu o cualquier otro numero para continuar")
			repeat=int(input())
	elif n1==3:
		while repeat!=0:
			div()
			print("Escribe 0 para volver al menu o cualquier otro numero para continuar")
			repeat=int(input())

