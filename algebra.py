import heapq as hq
import os
import time
import math

#Se debe tener en el archivo txt el orden de la matriz arriba de la matriz
#Para el metodo SEIDEL se debe sacar el comentario de la linea 29


def titulo():
	os.system('clear')
	print("      ************************************************")
	print("    ************* METODOS ITERATIVOS *******************")
	print("  ********************************************************")
	print("  ******************** ALGEBRA III ***********************")
	print("  ********************************************************")
	print("    ********** WLADIMIR ALBORNOZ LEYTON*****************")	
	print("      ************************************************\n")
 
def calculo(anterior, actual, margen):       # Resultado iteracion actual, anterior y rango que es el margen de error
	i=len(anterior)
	resto=0
	i-=1
	while(i+1):
		resto=resto+(actual[i]-anterior[i])**(2)  # Proceso del prod. interno con el anterior
		i-=1
	resto = math.sqrt(resto)
	if(resto<=margen):
		print("--> ", resto)
		return 0
	else:
		print("--> ", resto)
		time.sleep(0.5)
		return 1
	
def seidel(archivo):
	print("Usted a escogido el metodo GAUSS SEIDEL ")
	time.sleep(1)
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
				d[y] = float(contenido.pop(0))
				x=x+1
			else:
				a[y][x] = float(contenido.pop(0))
				x=x+1
		c[y]=float(contenido.pop(0))
		y=y+1
	anterior =[0 for x in range(coeficientes)]
	actual =[0 for x in range(coeficientes)]
	x=0
	y=0
	i=1
	j=0
	opcion=0
	print("Para trabajar utilizaremos las siguientes matrices: ")
	print("La matriz sin la diagonal ")
	for lista in a:
		print(lista)
	print("\nSolo la diagonal de la matriz ",d)
	print("\nLos resultados de cada ecuacion ", c,"\n")
	opcion=(input("Presione INTRO para iniciar las iteraciones..."))
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
	print("\nEncontramos el margen de error!! \nEn la iteracion nro. ",j ," \nLos valores aproximados : \n",actual)

def jacobi(archivo):
	print("Usted a escogido el metodo GAUSS JACOBI")
	time.sleep(1)
	margen1=float(input("Ingrese el margen de error a calcular : "))
	contenido1 = archivo.read().split();
	archivo.close()
	coeficientes1=int(contenido1.pop(0))
	print ("La matriz es de ",coeficientes1, " X " , coeficientes1)
	#Crear matriz de tamaño nodo*nodo
	a1 = [[0 for x in range(coeficientes1)]for x in range(coeficientes1)] #
	y1=0
	c1 =[0 for x in range(coeficientes1)]
	d1 =[0 for x in range(coeficientes1)]
	while(y1<coeficientes1):
		x1=0
		while(x1<coeficientes1):                                       #1 2 3
			if(x1==y1):
				a1[y1][x1] = int(0)
				d1[y1] = int(contenido1.pop(0))
				x1=x1+1
			else:
				a1[y1][x1] = int(contenido1.pop(0))
				x1=x1+1
		c1[y1]=int(contenido1.pop(0))
		y1=y1+1
	anterior1 =[0 for x in range(coeficientes1)]
	actual1 =[0 for x in range(coeficientes1)]
	x1=0
	y1=0
	i1=1
	j1=0
	opcion1=0
	print("Para trabajar utilizaremos las siguientes matrices: ")
	print("La matriz sin la diagonal ")
	for lista1 in a1:
		print(lista1)
	print("\nSolo la diagonal de la matriz ",d1)
	print("\nLos resultados de cada ecuacion ", c1,"\n")
	opcion1=(input("Presione INTRO para iniciar las iteraciones..."))
	while (i1):
		y1=0
		while(y1<coeficientes1):
			anterior1[y1]=actual1[y1]
			y1=y1+1
		y1=0
		while(y1<coeficientes1):
			x1=0
			aux1=float(0)
			while(x1<coeficientes1):
				aux1=aux1+a1[y1][x1]*anterior1[x1] #actual->seidel    anterior-> jacobi 
				x1=x1+1
			actual1[y1]=float((c1[y1]-aux1)/d1[y1])
			y1=y1+1
		i1=calculo(anterior1,actual1,margen1)
		j1=j1+1
	print("\nEncontramos el margen de error!! \nEn la iteracion nro. ",j1 ," siendo los valores aproximados : \n",actual1)		

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
	print("****************************")
	print("*                          *")
	print("*  1.- Gauss Jacobi        *")
	print("*  2.- Gauss Seidel        *")
	print("*                          *")
	print("****************************\n")
	ingresa=int(input("Ingrese el metodo que desea utilizar "))
	if ingresa == 1:
		jacobi(archivo)
	if ingresa == 2:
		seidel(archivo)


if __name__ == "__main__":
	op=1
	while (op==1):
		main()
		print("\n*****************************")
		print("*                           *")
		print("*  1.- Volver a trabajar    *")
		print("*  0.- Salir                *")
		print("*                           *")
		print("*****************************\n")
		op=int(input(" Ingrese su opcion :"))
		while(op!=1 and op!=0):
			print("Error, ingrese una opcion valida porfavor")
			op=int(input(" Ingrese su opcion "))