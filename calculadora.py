from os import system

opcion= "s"
dato = float(0)
valor1 = int(0)
valor2 = int(0)
divisorCero = "s"
from matematica.aritmetica import sumar, multiplicar, restar, dividir, calculoArea, raizCuadrada
# se puede usar la siguiente opcion en este caso
# from matematica.aritmetica import *

while opcion == "s":
    
    operacion=input("Que operacion desea realizar? \n(1) Suma \n(2) Resta \n(3) Multiplicacion \n(4) Division \n(5) Raiz Cuadrada \n(6) Calculo de Area \n")

    if operacion=="1":
        print("ingrese los 2 valores a sumar")
        valor1=int(input("ingresa el primer numero:"))
        valor2=int(input("Ingresa el segundo numero:"))
        dato = sumar(valor1,valor2)
        solucion = f"el resultado de la suma es {dato}"
    elif operacion =="2":
        print("ingrese los 2 valores a restar")
        valor1=int(input("ingresa el primer numero:"))
        valor2=int(input("Ingresa el segundo numero:"))
        dato = restar(valor1,valor2)
        solucion = f"el resultado de la multiplicacion es {dato}"
    elif operacion =="3":
        print("ingrese los 2 valores a restar")
        valor1=int(input("ingresa el primer numero:"))
        valor2=int(input("Ingresa el segundo numero:"))
        dato = multiplicar(valor1,valor2)
        solucion = f"el resultado de la multiplicacion es {dato}"
    elif operacion =="4":
        valor2=0
        while valor2==0:
            print("ingrese los 2 valores a dividir")
            valor1=int(input("ingresa el primer numero:"))
            valor2=int(input("Ingresa el segundo numero:"))
            if valor2 == 0:
                print("el segundo numero no puede ser 0")
        dato = (dividir(valor1,valor2))
        solucion = f"el resultado de la division es {dato:.2f}"
    elif operacion =="5":
        print("ingrese el valor")
        valor1=int(input("ingresa el numero:"))
        dato = (raizCuadrada(valor1))
        solucion = f"La raiz cuadrada de {valor1} es {dato:.4f}"
    elif operacion =="6":
        print("ingrese el valor de radio del circulo")
        valor1=int(input("ingresa el primer numero:"))
        dato = (calculoArea(valor1))
        solucion = f"el area de la circunferencia es es {dato:.4f}"
    else:
        solucion = "la opcion que ingresaste era incorrecta"

    print(solucion)

    opcion=input("desea otra operacion (s/n):")
    system("cls")