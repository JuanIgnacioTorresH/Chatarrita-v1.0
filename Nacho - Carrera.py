#Esta version hace todo el recorrido en diagonales, no se si es muy practico
from machine import Pin
import time

In3 = Pin (13, Pin.OUT)
In3 = Pin (12, Pin.OUT)
In3 = Pin (11, Pin.OUT)
In3 = Pin (10, Pin.OUT)
infr1 = Pin (6, Pin.IN)
infr2 = Pin (7, Pin.IN)
#Delanteros
infr3 = Pin (8, Pin.IN)
#Trasero Izq
infr4 = Pin (9, Pin.IN)
#Trasero Derecho

def move_forward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    #Funcion para ir adelante

def turn_right():
    In1.low()
    In2.low()
    In3.low()
    In4.high()
    #Funcion para girar a la derecha


def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    #Funcion para detenerse

while True:
    if infr1.value() == 1 or infr3.value() == 1:
        #Funcion si los infrarojos izquierdos detectan el borde de la pista
        stop()
        sleep_us(2)
        #Paro a chatarrita
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 1: #El 1 seria la cantidad de segundos que le quiero dar, eso hay que probarlo.
            turn_right()
        #Giras a la derecha por tantos segundos (el 1)
        move_forward()
        #Seguis avanzando
    else:
        move_forward()
        #Si no hay giros que hacer, sigue avanzando
    
    if infr2.value() == 1 or infr4.value() == 1:
        #Funcion si los infrarojos derechos detectan el borde de la pista
        stop()
        sleep_us(2)
        #Paro a chatarrita
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 1: #El 1 seria la cantidad de segundos que le quiero dar, eso hay que probarlo.
            turn_left()
        #Giras a la izq por tantos segundos (eso seria el 1)
        move_forward()
        #Seguis avanzando
    else:
        move_forward()
        #Si no hay que girar seguis avanzando