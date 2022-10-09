from statistics import mode
print("Programa para calcular moda, media y mediana")
op=0

zero=1
moda=0
acumulador=0
mediana=0
Lista=[]

while op!=4:
	Lista.clear()
	mediana=0
	acumulador=0
	print("Ingresa 1 para media, 2 para moda, 3 para mediana ")
	op=int(input("Opcion:"))
	if op==1:	
		#pedir dato
		while True:
			try:
				print("Escribe cuantos numeros vas a ingresar a la lista")
				f=int(input())
				while f==0:
					print("No es posible asignar 0 datos")
					print("Escribe cuantos numeros vas a ingresar a la lista")
					f=int(input("Cantidad:"))
				break
			except ValueError:
				print("Favor de ingresar un numero")
		for i in range(f):
			lista=int(input("Dato " + str(i+1) +": "))
			Lista.append(lista)
			acumulador=acumulador+lista
		for i in Lista:
			print(i)
		media=acumulador/f
		print("La media es: " + str(media))
	elif op==3:
		while True:
			try:
				print("Escribe cuantos numeros vas a ingresar a la lista")
				f=int(input())
				while f==0:
					print("No es posible asignar 0 datos")
					print("Escribe cuantos numeros vas a ingresar a la lista")
					f=int(input("Cantidad:"))
				break
			except ValueError:
				print("Favor de ingresar un numero")
		for i in range(f):
			lista=int(input("Dato " + str(i+1) +": "))
			Lista.append(lista)
		medianapos=(f+1)/2
		if f % 2==0:
			print("La mediana es: " )
			mediana=mediana+Lista[int(medianapos)] 
			print(mediana)
			mediana=mediana+Lista[int(medianapos-1)]
			print(mediana)
			mediana=mediana/2
			print(mediana)
		else: 
			print("La mediana es: " )
			print(Lista[int(medianapos-1)])
	elif op==2:
		while True:
			try:
				print("Escribe cuantos numeros vas a ingresar a la lista")
				f=int(input())
				while f==0:
					print("No es posible asignar 0 datos")
					print("Escribe cuantos numeros vas a ingresar a la lista")
					f=int(input("Cantidad:"))
				break
			except ValueError:
				print("Favor de ingresar un numero")
		for i in range(f):
			lista=int(input("Dato " + str(i+1) +": "))
			Lista.append(lista)
		
		print("La moda es :",  mode(Lista))

	