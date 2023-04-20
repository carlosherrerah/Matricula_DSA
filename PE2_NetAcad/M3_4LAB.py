
#------------------------------------------------------------------------------
# LAB La clase Timer
'''
def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

class Timer:
    def __init__(self, hh=0, mm=0, ss=0):
        # Escribir código aquí
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        # Escribir código aquí
        # return ("%05d"%self.cadena)       # int
        # return self.cadena.rjust(5,'0')   # str
        # return ("%02d"%self.hh+":"+"%02d"%self.mm+":"+"%02d"%self.ss)
        return two_digits(self.hh) + ":" + \
                    two_digits(self.mm) + ":" + \
                    two_digits(self.ss)    


    def next_second(self):
        # Escribir código aquí
        self.ss+=1
        if self.ss >= 60:
            self.ss = 0
            self.mm+=1
            if self.mm >= 60:
                self.mm= 0
                self.hh+=1
                if self.hh >= 24:
                    self.hh = 0
                    self.ss=0

    def prev_second(self):
        # Escribir código aquí
        self.ss-=1
        if self.ss <= -1:
            self.ss = 59
            self.mm-=1
            if self.mm <= -1: 
                self.mm= 59
                self.hh-=1
                if self.hh <= -1:
                    self.hh = 23
     

timer = Timer(23, 59,59)
print(timer)

timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)

print("-")
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
'''

#------------------------------------------------------------------------------
# LAB Días de la semana
'''
class WeekDayError(Exception):
    pass

class Weeker:
    # Escribir código aquí.
    valores = "Lun Mar Mie Jue Vie Sab Dom"
    valor = valores.split()

    def __init__(self, day):
        # Escribir código aquí.
        try:
            self.porcion = Weeker.valor.index(day)
        except ValueError:
            raise WeekDayError
        
        # if day not in Weeker.valor:
        #     raise WeekDayError
        # self.vuelta = 0
        # self.porcion = Weeker.valor.index(day)

    def __str__(self):
        # Escribir código aquí.
        return Weeker.valor[self.porcion]

    def add_days(self, n):
        # Escribir código aquí.
        pos = self.porcion
        self.vuelta  = (pos + n) // 7
        self.porcion = (pos + n) % 7        

    def subtract_days(self, n):
        # Escribir código aquí.
        pos = self.porcion
        self.vuelta  = (pos - n) // 7
        self.porcion = (pos - n) % 7        

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
'''

#------------------------------------------------------------------------------
# LAB Puntos en un plano
'''
# {\displaystyle d={\sqrt {(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}}.}
# {\displaystyle (x',y')=((x\cos \theta -y\sin \theta \,),(x\sin \theta +y\cos \theta \,)).}                

# https://docs.python.org/3.7/library/math.html#trigonometric-functions
# math.hypot(x, y) =  sqrt(x*x + y*y)

import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        # Escribir código aquí
        self.x = x
        self.y = y

    def getx(self):
        # Escribir código aquí
        return self.x

    def gety(self):
        # Escribir código aquí
        return self.y

    def distance_from_xy(self, x, y):
        # Escribir código aquí
        return math.hypot(self.getx() - x , self.y - y)
    

    def distance_from_point(self, point):
        # Escribir código aquí
        return self.distance_from_xy(point.getx(), point.gety())
        #return math.hypot(self.getx() - point.x , self.y - point.y)

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
'''

#------------------------------------------------------------------------------
# LAB Triangulo




