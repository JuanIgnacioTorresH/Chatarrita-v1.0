#Esta version hace todo el recorrido en diagonales, no se si es muy practico
from machine import Pin, ADC
import time

In1 = Pin (13, Pin.OUT)
In2 = Pin (12, Pin.OUT)
In3 = Pin (11, Pin.OUT)
In4 = Pin (10, Pin.OUT)
#Pines de motores

infr1 = ADC(Pin(27))
#infrarojo izquierdo
infr2 = ADC(Pin(28))
#infrarojo derecho
infr3 = ADC(Pin(26))
#infrarojo delantero
ivalue1 = 0
ivalue2 = 0
ivalue3 = 0
#valores de ADC de los infrarojos

def move_forward():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    #Funcion para ir adelante

def turn_right():
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    #Funcion para girar a la derecha

def turn_left():
    In1.high()
    In2.low()
    In3.high()
    In4.high()
    #Funcion para girar a la derecha

def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    #Funcion para detenerse

time1 = 0
#variable para guardar tiempos de referencia
def position_init():
    ivalue3 = ((infr3.read_u16())*3) / 65336
    stop()
    sleep_us(2)
    time1 = utime_ticks_s()
    while utime_ticks_diff(utime_ticks_s - time1) < 5:
        turn_right()
        #Giro a la derecha lo suficiente como para que doble 180 grados a la derecha
    sleep_us (2)
    if ivalue3 <= 3:
        while ivalue3 <= 3:
            move_forward()
            #Se mueve hasta llegar al borde
        stop()
    while utime_ticks_diff(utime_ticks_s - time1) < 5:
        turn_left()
        #Giro suficiente como para que se centre de vuelta
    stop()
#Inicia la posicion inicial, dirigiendo a chatarrita al borde derecho de la pista


position_init()            
while True:
    ivalue1 = ((infr1.read_u16())*3) / 65336
    ivalue2 = ((infr2.read_u16())*3) / 65336
    sleep_us(2)
    move_forward()
    if ivalue1() <= 3:
        #Funcion si los infrarojos izquierdos detectan que se estan tocando parte negra de la pista, lo que signfica que hay un giro a la izquierda
        stop()
        sleep_us(2)
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 1:
            turn_left()
    
    if infr2.value() >= 3:
        #Funcion si los infrarojos derechos detectan que se estan tocando parte negra de la pista, lo que signfica que hay un giro a la derecha
        stop()
        sleep_us(2)
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 1:
            turn_right()
