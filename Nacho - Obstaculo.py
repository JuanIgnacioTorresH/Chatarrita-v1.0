from machine import Pin, ADC
import time
#Importo las funciones para no tener que escribir tanto

trigger = Pin(20, Pin.OUT)
echo = Pin (21, Pin.IN)
infr = ADC(Pin(26))
ivalue1 = 0
#Asigno pines del ultrasonido y del infrarojo

In1 = Pin (13, Pin.OUT)
In2 = Pin (12, Pin.OUT)
In3 = Pin (11, Pin.OUT)
In4 = Pin (10, Pin.OUT)
#Checkea que sean esos los pines para cada uno, asigne a cualquiera

EN_A = Pin (14, Pin.OUT)
EN_B = Pin (9, Pin OUT)
EN_A.high()
EN_B.high()
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
    In3.low()
    In4.high()
    #Funcion para ir adelante

def move_backwards():
    In1.low()
    In2.high()
    In3.high()
    In4.low()

def turn_right():
    In1.low()
    In2.high()
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
    ivalue = ((infr.read_u16())*3) / 65336
    if distancia < 150:
        #150 siendo el tamano total de la pista
        if infr.value() >= 3:
            #Necesito la tension umbral para distinguir entre blanco y negro, usando 3 como ejemplo
            while infr.value() == 3:
                move_forward()
                #Si detecta algo y el infrarojo detecta que todavia no va a estar fuera del cuadrante, el robot avanza
    
        stop()
        sleep_us(2)
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 1:
            move_backwards()
        sleep_us(2)
        stop()
        sleep_us(2)
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 5:
            turn_right() 
        sleep_us(2)
        #Si detecta que hay un objeto pero este en zona negra, o ya estaba llevando un objeto y alcanzo el borde, se detiene, va para atras un segundo y deberia dar un giro de 180(dar variable) 
    else:
        time1 = utime_ticks_s()
        while utime_ticks_diff(utime_ticks_s - time1) < 1:
            turn_right()
        sleep_us(2)
        stop()
        sleep_us (2)
        #Si no detecta nada, va a girar a la derecha por 1 segundo, detenerse y comenzar el ciclo de nuevo
