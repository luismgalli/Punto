
import math

class Punto:

    def __init__(self, x, y):
        self._x = x
        self._y = y

        
    def constructor(self):
        
        self._punto = (self._x,self._y) 
        print(self._punto)
        pass

    def cuadrante(self):
        if self._x == 0 and self._y != 0:
            print('Su punto se encuentra sobre el eje Y')
        elif self._x != 0 and self._y ==0 :
            print('Su punto se encuentra sobre el eje X')
        elif self._x ==0 and self._y ==0:
            print('Su punto se encuentra sobre el origen')
        elif self._x > 0 and self._y >0 :
            print('Su punto se encuentra en el primer cuadrante')
        elif self._x > 0 and self._y <0 :
            print('Su punto se encuentra en el segundo cuadrante')
        elif self._x < 0 and self._y <0 :
            print('Su punto se encuentra en el tercer cuadrante')
        else:
            print('Su punto se encuentra en el cuarto cuadrante')
        pass

    def vector(self,x1,y1):
        
        self._punto1 = (x1,y1) 
        print('Su otro punto es. ' + str(self._punto1))
        self._vector = (y1-self._y,x1-self._x)
        print('Su vector es :' + str(self._vector))
        pass

    def distancia(self,x1,y1):
        self._distance = math.sqrt((x1-self._x)**2+(y1-self._y)**2)
        print(self._distance)
        pass





class Rectangulo:


    def __init__(self,a,b,a1,b1):
        self._a = a
        self._b = b
        self._a1 = a1
        self._b1 = b1
        self._diagonal = (self._b1-self._b,self._a1-self._a)
        print('La diagonal de su rectangulo es :' + str(self._diagonal))      
        
    def constructor(self):
        punto = (self._a,self._b)
        punto1 = (self._a1,self._b1)
        print('1er punto: ' + str(punto))
        print('2do punto: ' + str(punto1))
        pass

    def base(self):
        #modulo = math.sqrt(self._diagonal[0]**2+self._diagonal[1]**2)
        self._basesita = int(abs(self._a-self._a1))
        print('La base de su rectangulo es :' + str(self._basesita))
        pass

    def altura(self):
        self._alturita = int(abs(self._b-self._b1))
        print('La altura de su rectangulo es :' + str(self._alturita))
        pass

    def area(self):
        self._areasita = self._alturita*self._basesita
        print('La area de su rectangulo es :' + str(self._areasita))
        pass
