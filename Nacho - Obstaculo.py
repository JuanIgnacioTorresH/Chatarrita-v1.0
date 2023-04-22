from machine import Pin
import time
#Importo las funciones para no tener que escribir tanto

trigger = Pin(27, Pin.OUT)
echo = Pin (26, Pin.IN)
infr = Pin (7, Pin.IN)
#Asigno pines del ultrasonido y del infrarojo

In3 = Pin (13, Pin.OUT)
In3 = Pin (12, Pin.OUT)
In3 = Pin (11, Pin.OUT)
In3 = Pin (10, Pin.OUT)
#Asigno pines de las ruedas

EN_A = Pin (14, Pin.OUT)
EN_B = Pin (9, Pin OUT)
EN_A.high()
EN_B_high()
#Habilitadores

def ultra ():
    trigger.low()
    sleep_us (2)
    #Aseguro que el trigger este en 0
    trigger.high()
    sleep_us (5)
    trigger.low()
    #Mando el pulso prendiendo y apagando el trigger
    pulse = time_pulse_us(echo, Pin.high)
    #Pongo el valor del tiempo que tarda el pulso en ir y venir
    distance = pulse * 0.0343 / 2
    #Calculo la distancia como el tiempo del pulso por la velocidad de la senal en el aire (que me daria la distancia de ida y vuelta) divido a dos (para tomar el valor de una sola)
    return distance
    #Devuelvo al programa principal el valor de distancia
    
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
    ultra()
    #Uso la funcion de ultrasonido para ver si tengo cajas en frente
    if distancia < 150:
        #Asumo que la distancia maxima para que hayan obstaculos es 150
        if infr.value() == 0:
            while infr.value() == 0:
                move_forward()
                #Si detecta algo y el infrarojo detecta que todavia no va a estar fuera del cuadrante, el robot avanza
        else:
            stop()
            #Si detecta que hay algo, pero esta por irse del cuadrante, da prioridad a detenerse
    else:
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 1:
            turn_right()
        stop()
        sleep_us (2)
        #Si no detecta nada, va a girar a la derecha por 1 segundo, detenerse y comenzar el ciclo de nuevo