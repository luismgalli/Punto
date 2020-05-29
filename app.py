from Clase import Punto
from Clase import Rectangulo
import math


print("\nHola, este es el menu del sistema de coordenadas.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: Para agregar un punto.
- Type 2: Para saber en donde se encuentra su punto.
- Type 3: Para crear un vector.
- Type 4: Para saber la distancia entre los dos puntos.
- Type 5: Para crear un rectangulo.
- Type 6: Para salir del menu.
    ''')

    option = int(input("Enter a number:"))
    if option == 1:
        print('Ingrese su punto (x,y)')
        print('Ingrese x')
        chek_x = input()
        x = float(chek_x) if chek_x != '' else 0
        print('Ingrese y')
        chek_y = input()
        y = float(chek_y) if chek_y != '' else 0
        puntico = Punto(x=x, y=y)
        puntico.constructor()
        pass
    elif option ==2:
       puntico.cuadrante()
       pass
    elif option ==3:
        print('Ingrese su otro punto (x1,y1)')
        print('Ingrese x1:')
        chek_x1 = input()
        x1 = float(chek_x1) if chek_x1 != '' else 0
        print('Ingrese y1')
        chek_y1 = input()
        y1 = float(chek_y1) if chek_y1 != '' else 0
        puntico.vector(x1,y1)
        pass
    elif option == 4:
        puntico.distancia(x1,y1)
        pass
    elif option ==5: 
        rectangulito = Rectangulo(a=x,b=y,a1=x1,b1=y1)
        rectangulito.constructor()
        rectangulito.base()
        rectangulito.altura()
        rectangulito.area()
        pass
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))