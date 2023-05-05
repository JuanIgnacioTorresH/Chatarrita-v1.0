#Esta version hace giros mas smooth(modificar)
from machine import Pin, PWM
import time

nein = (insertar numero que permita dar 90 a un lado)

In1 = Pin (13, Pin.OUT)
In2 = Pin (12, Pin.OUT)
In3 = Pin (11, Pin.OUT)
In4 = Pin (10, Pin.OUT)
infr1 = Pin (6, Pin.IN)
infr2 = Pin (7, Pin.IN)
#Delanteros
infr3 = Pin (8, Pin.IN)
#Trasero Izq
infr4 = Pin (9, Pin.IN)
#Trasero Derecho

EN_B= machine.PWM (machine.Pin(27))
EN_A= machine.PWM (machine.Pin(26))
#variables que regulan el pwm del motor A y B respectivamente.
EN_A.freq(10000)
EN_B.freq(10000)
#frecuencia con la que va a trabajar.
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)
#velocidad maxima con la que va a trabajar los motores.

def forward():
    #funcion para que el robot se mueva hacia adelante.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)
    In1.value(1)
    In2.value(0)
    In3.value(0)
    In4.value(1)
    
def backward():
    #funcion para que el robot se mueva hacia atras.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)
    In1.value(0)
    In2.value(1)
    In3.value(1)
    In4.value(0)

def right():
    #funcion para que el robot se mueva hacia la derecha.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)
    In1.value(0)
    In2.value(1)
    In3.value(0)
    In4.value(1)

def left():
    #funcion para que el robot se mueva hacia la izquierda.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(65025)    
    In1.value(1)
    In2.value(0)
    In3.value(1)
    In4.value(0)


def dderforw():
    #funcion para que el robot se mueva de forma diagonal hacia la derecha.
    EN_A.duty_u16(65025)
    EN_B.duty_u16(45025)
    In1.value(1)
    In2.value(0)
    In3.value(0)
    In4.value(1)

    def dderback():
    #funcion para que el robot se mueva de forma diagonal hacia la derecha, pero hacia atras.
    EN_A.duty_u16(65025)
    EN_B.duty_u16(45025)
    In1.value(0)
    In2.value(1)
    In3.value(1)
    In4.value(0)

def dizqforw():
    #funcion para que el robot se mueva de forma diagonal hacia la izquierda.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(45025)
    In1.value(1)
    In2.value(0)
    In3.value(0)
    In4.value(1)

def dizqback():
    #funcion para que el robot se mueva de forma diagonal hacia la izquierda, pero hacia atras.
    EN_B.duty_u16(65025)
    EN_A.duty_u16(45025)
    In1.value(0)
    In2.value(1)
    In3.value(1)
    In4.value(0)

def stop():
    In1.value(0)
    In2.value(0)
    In3.value(0)
    In4.value(0)

def position_init()
    time1 = utime_ticks_s()
    while utime_ticks_diff(utime_ticks_s - time1) < nein:
        right()
        #Giras a la derecha por tantos segundos. la idea seria ajuistarlo para que gire 90�
    if infr1.value() == 0 and infr2.value() == 0:
        while infr1.value() == 0 or infr2.value() == 0:
            if In1.value == 0 or In4.value == 0 or In3.value == 1 or In2.value == 1:
                forward()
                #Se mueve hasta llegar al borde
    time1 = utime_ticks_s()
    while utime_ticks_diff(utime_ticks_s - time1) < nein:
        left()
        #Giras a la  por tantos segundos. la idea seria ajuistarlo para que gire 90� en sentido contrario
    sleep_us (2)
    #Puesta en posicion  

position_init()

while True:
    position_init()
    forward()
    if infr2.value() == 0:
        stop()
        sleep_us (2)
        EN_B.duty_u16(45025)
        right()
        vel = 45025
        while infr2.value() == 0:
            vel = vel + 100
            EN_B.duty_u16(45025)
            EN_B.duty_u16(vel)
            sleep_us (2)
    if infr1.value() == 1: 
        stop()
        sleep_us (2)
        EN_A.duty_u16(45025)
        left()
        vel = 45025
        while infr1.value() == 1:
            left()
            sleep_us (2)
            EN_A.duty_u16(45025)
            vel = 45025
            while infr2.value() == 0:
            vel = vel + 100
            EN_A.duty_u16(45025)
            EN_A.duty_u16(vel)