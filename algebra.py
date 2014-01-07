import heapq as hq
import os
import time
import math
# os.system('clear') si se ejecuta el programa en linux
def titulo():
	os.system('clear')
	print("")
	print("        ********************************************")
	print("      ************************************************")
	print("    ************* METODOS ITERATIVOS *******************")
	print("  ********************************************************")
	print(" ********************** ALGEBRA III ***********************")
	print("  ********************************************************")
	print("    ********** WLADIMIR ALBORNOZ LEYTON*****************")	
	print("      ************************************************")
	print("        **************** SEIDEL ********************\n")


def calculo(anterior, actual, margen):       # Resultado iteracion actual, anterior y rango que es el margen de error
	i=len(anterior)
	resto=0
	i-=1
	while(i+1):
		resto=resto+(actual[i]-anterior[i])**(2)  # Proceso del prod. interno con el anterior
		i-=1
	resto = math.sqrt(resto)
	if(resto<=margen):
		return 0
	else:
		print("--> ", resto)
		time.sleep(0.5)
		return 1
		
def main():

	correcto=True
	while(correcto):
		titulo()
		nombre=input("Ingrese el nombre del archivo: ")
		try:
			 archivo = open(nombre,'r')
			 correcto = False
		except IOError:
			 print("Error, Intentelo nuevamente")
			 time.sleep(1.6)
			 os.system('clear')
			 titulo()
	margen=float(input("Ingrese el margen de error a calcular : "))
	contenido = archivo.read().split();
	archivo.close()
	coeficientes=contenido.pop(0)
	coeficientes=int(coeficientes)
	print ("La matriz es de ",coeficientes, " X " , coeficientes)
	#Crear matriz de tamaño nodo*nodo
	a = [[0 for x in range(coeficientes)]for x in range(coeficientes)] #
	y=0
	c =[0 for x in range(coeficientes)]
	d =[0 for x in range(coeficientes)]
	while(y<coeficientes):
		x=0
		while(x<coeficientes):                                       #1 2 3
			if(x==y):
				a[y][x] = int(0)
				d[y] = int(contenido.pop(0))
				x=x+1
			else:
				a[y][x] = int(contenido.pop(0))
				x=x+1
		c[y]=int(contenido.pop(0))
		y=y+1
	anterior =[0 for x in range(coeficientes)]
	actual =[0 for x in range(coeficientes)]
	x=0
	y=0
	i=1
	j=0
	print("Para trabajar utilizaremos las siguientes matrices: ")
	print("La matriz sin la diagonal ")
	for lista in a:
		print(lista)
	print("\nSolo la diagonal de la matriz ",d)
	print("\nLos resultados de cada ecuacion ", c,"\n")
	print("A continuacion se iniciaran las iteraciones...")
	while (i):
		y=0
		while(y<coeficientes):
			anterior[y]=actual[y]
			y=y+1
		y=0
		while(y<coeficientes):
			x=0
			aux=float(0)
			while(x<coeficientes):
				aux=aux+a[y][x]*actual[x] #actual->seidel    anterior-> jacobi 
				x=x+1
			actual[y]=float((c[y]-aux)/d[y])
			y=y+1
		i=calculo(anterior,actual,margen)
		j=j+1
	print("\nEncontramos el margen de error!! \nEn la iteracion nro. ",j ," siendo los valores aproximados : \n",actual)

if __name__ == "__main__":
	usuario=1
	while (usuario):
		main()
		usuario=int(input("\nPresione 0 para salir \nPresione 1 para volver a trabajar : "))
		
