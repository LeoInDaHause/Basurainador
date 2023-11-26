from tcs3200 import TCS3200 
import i2c_lcd #16 por fila y 2 columnas
from servo import Servo
from machine import Pin, I2C, deepsleep, PWM
import time
import utime
from neopixel import NeoPixel
import random

#Contador Objetos
co=0
cp=0
cm=0

ob=1

# Variable para manejar la pantalla grove LCD RGB backlight V2.0

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

# configuaracion del dispaly para manejar correctamente los datos

d = i2c_lcd.Display(i2c, lcd_addr=0x3e, rgb_addr=0x62)

# Funcion necesaria para manejar los datos

d.home()

# funcion para borrar esos datos (no mostrar estos datos en la pantalla)

d.clear()

# Pines que se van a utilizar para el sensor TCS3200

tcs3200 = TCS3200(OUT=19, S2=5, S3=18, S0=17, S1=16, LED=10)

# Pines utilizados para los leds

ledb=Pin(32, Pin.OUT)
ledi=Pin(33, Pin.OUT)

ledb.off()
ledi.off()

p26 = Pin(26, Pin.OUT)
pwm = PWM(p26)
pwm.freq(40000)

# Pin para manejar el servo

my_servo = Servo(pin_id=14)

# posicion inicial del servo, 0 = grados

my_servo.write(0)

# sale de la libreria para manejar y calibrar correctamente el sensor TCS3200

tcs3200.debugging=tcs3200.ON
tcs3200.led = tcs3200.ON

NEOPIXEL_PIN=20
NO_OF_LEDS=7

neoPixel = NeoPixel(Pin(NEOPIXEL_PIN),NO_OF_LEDS)
tcs3200.freq_divider = tcs3200.TWO_PERCENT

# Calibrar el sensor en una frecuencia de negro y blanco, lo solicito lo solicita la libreria

black_freq = [2890.257, 2601.051, 3495.77, 9454.477]
white_freq = [15283.51, 15494.27, 14985.76, 11150.76]
tcs3200.calibrateSet(black_freq,white_freq)

# Funcion para que la pantalla LCD, varie 2 veces entre los colores azul, verde, rojo y despues quede en color gris

def color():
    for i in range(2):
        d.color(0, 0, 255)  # Azul
        time.sleep(0.5)
        d.color(0, 255, 0)  # Verde
        time.sleep(0.5)
        d.color(255, 0, 0)  # Rojo
        time.sleep(0.5)
    d.color(128, 128, 128)
    
# la funcion random_color y celebrate hace que cuando el usuario ya halla propiciado el elemento correcto, la pantalla,
# parpadea de diferentes colores
    
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def celebrate(display, servo, duration):
    end_time = time.time() + duration
    my_servo.write(95)  # aca hace que el servomotor se mueva
    while time.time() < end_time:
        color = random_color()
        display.backlight.set_color(*color)
        time.sleep(0.5)
    my_servo.write(0)  # aca hace que el servomotor se mueva
    
def celebrate2(display, servo, duration):
    end_time = time.time() + duration
    my_servo.write(0)
    sleep_time = duration / 90  # divide the duration by the number of degrees
    for angle in range(90):  # loop from 0 to 90
        if time.time() > end_time:
            break
        color = random_color()
        display.backlight.set_color(*color)
        my_servo.write(angle)  # write the current angle to the servo
        time.sleep(sleep_time)  # sleep for the calculated time
    
def sonido_acierto():
    pwm = PWM(p26)
    pwm.freq(40000000)  # Frecuencia de 40 MHz
    pwm.duty(512) 
    notas2=[523, 659, 784, 880, 0, 880, 784, 659, 523]
    for nota in notas2:
        if nota != 0: # Si la nota es 0, hace una pausa
            pwm.freq(nota) # Cambia la frecuencia del PWM a la de la nota
        else:
            pwm.duty(0) # Si la nota es 0, detiene el PWM
        time.sleep(0.1) # Espera un poco antes de reproducir la siguiente nota
        pwm.duty(512) # Reinicia el ciclo de trabajo del PWM para la siguiente nota
    pwm.deinit()
    
def sonido_desacierto():
    pwm = PWM(p26)
    pwm.freq(40000000)  # Frecuencia de 40 MHz
    pwm.duty(512) 
    notas3 = [523, 494, 466, 440, 0, 440, 466, 494, 523]
    for nota in notas3:
        if nota != 0: # Si la nota es 0, hace una pausa
            pwm.freq(nota) # Cambia la frecuencia del PWM a la de la nota
        else:
            pwm.duty(0) # Si la nota es 0, detiene el PWM
        time.sleep(0.1) # Espera un poco antes de reproducir la siguiente nota
        pwm.duty(512) # Reinicia el ciclo de trabajo del PWM para la siguiente nota
    pwm.deinit()
    
def sonido_fiesta():
    pwm = PWM(p26)
    pwm.freq(40000000)  # Frecuencia de 40 MHz
    pwm.duty(512) 
    notas3 = [294,0,294,587,587,587,440,440,440,0,415,415,0,392,392,0,349,349,0,294,349,349,392,262,0,262,587,587,587,440,440,440,0,415,415,0,392,392,0,349,349,0,294,349,349,392,247,0,247,587,587,587,440,440,440,0,415,415,0,392,392,0,349,349,0,294,349,349,392,233,0,233,587,587,587,440,440,440,0,415,415,0,392,392,0,349,349,0,294,349,349,392,]
    for nota in notas3:
        if nota == 0: # Si la nota es 0, hace una pausa
            continue
        pwm.freq(nota) # Cambia la frecuencia del PWM a la de la nota
        time.sleep(0.07) # Espera un poco antes de reproducir la siguiente nota
        pwm.duty(512) # Reinicia el ciclo de trabajo del PWM para la siguiente nota
    pwm.deinit()
    
# Funcion para crear un random entre los valores del 1 al 3, que muestre en la pantalla el mensaje "Ingrese un elemento papel o cartón" ,
#"Ingrese un elemento organico"   o "Ingrese un elemento plástico, metal o vidrio"
    
def assign_random_number():
    ledb.off()
    ledi.off()
    global P, O, M, rojo, verde, azul
    if co<ob and cp<ob and cm<ob:
        numero = random.randint(1, 3)
    if co>=ob and cp<ob and cm<ob:
        numero = random.choice([1, 3])
    if cp>=ob and co<ob and cm<ob:
        numero = random.randint(2, 3)
    if cm>=ob and cp<ob and co<ob:
        numero = random.randint(1, 2)
    
    if co>=ob and cp>=ob and cm<ob:
        numero = 3
    if cp>=ob and cm>=ob and co<ob:
        numero = 2
    if cm>=ob and co>=ob and cp<ob:
        numero = 1
    
    if co==ob and cp==ob and cm==ob:
        d.clear()
        d.write('GANASTE!! :D')
        sonido_fiesta()
        celebrate2(d, my_servo, 3)
        time.sleep(3)
        deepsleep()
    elif numero == 1:
        print('Ingrese un elemento papel o cartón')
        d.home()
        d.clear()
        d.write('Ingrese P o C')   # lo muestra en la pantalla LCD
        color()
        P=True
        O=False
        M=False
        rojo=False
        verde=False
        azul=False
    elif numero == 2:
        print('Ingrese un elemento organico')
        d.home()
        d.clear()
        d.write('Ingrese O')   # lo muestra en la pantalla LCD
        color()
        P=False
        O=True
        M=False
        rojo=False
        verde=False
        azul=False
    elif numero == 3:
        print('Ingrese un elemento P, M o V')
        d.home()
        d.clear()
        d.write('Ingrese P, M o V')   # lo muestra en la pantalla LCD
        color()
        P=False
        O=False
        M=True
        rojo=False
        verde=False
        azul=False

assign_random_number()
time.sleep(1)

# esto es lo que va a hacer el programa como tal, todo el tiempo

while True:
    print(co,cp,cm)

    
    time.sleep(2)  # en un tiempo de 2 segundo el sensor va a tomar datos RGB
    rgb = tcs3200.rgb
    for i in range(NO_OF_LEDS):
        neoPixel[i] = (rgb[0],rgb[1],rgb[2])
    neoPixel.write()
    if rgb[0]>10 and rgb[0]>rgb[1] and rgb[0]>rgb[2]:  # es ROJO, si se cumplen las condiciones
        rojo=True
        verde=False
        azul=False
        print('Rojo')
    if rgb[2]>10 and rgb[2]>rgb[1] and rgb[2]>rgb[0]:  # es AZUL, si se cumplen las condiciones
        verde=False
        azul=True
        rojo=False
        print('Azul')
    if rgb[1]>20 and rgb[1]>rgb[0] and rgb[1]>rgb[2]:  # es VERDE, si se cumplen las condiciones
        verde=True
        azul=False
        rojo=False
        print('Verde')
    if O==True:
        if verde==True:
            print("Correcto")
            d.home()
            d.clear()
            d.write('¡Correcto!')  # imprime en la pantalla "CORRECTO"
            co+=1
            sonido_acierto()
            celebrate(d, my_servo, 3)  # Celebrar durante 3 segundos y el servo se mueve
            time.sleep(1)
            ledb.on()
            ledi.off()
            assign_random_number()
            
        elif azul==True or rojo==True:
            print("Incorrecto")
            d.home()
            d.clear()
            d.write('Incorrecto :(')  # Imprime en la pantalla "INCORRECTO"
            d.color(255, 255, 0)
            sonido_desacierto()
            time.sleep(3)
            ledb.off()
            ledi.on()
            assign_random_number()
    if M==True:
        if rojo==True:
            print("Correcto")
            d.home()
            d.clear()
            d.write('¡Correcto!')  # imprime en la pantalla "CORRECTO"
            cm+=1
            sonido_acierto()
            celebrate(d, my_servo, 3)  # Celebrar durante 3 segundos y el servo se mueve
            time.sleep(1)
            ledb.on()
            ledi.off()
            assign_random_number()
        elif azul==True or verde==True:
            print("Incorrecto")
            d.home()
            d.clear()
            d.write('Incorrecto :(')  # Imprime en la pantalla "INCORRECTO"
            d.color(255, 255, 0)
            sonido_desacierto()
            time.sleep(3)
            ledb.off()
            ledi.on()
            assign_random_number()
    if P==True:
        if azul==True:
            print("Correcto")
            d.home()
            d.clear()
            d.write('¡Correcto!')  # imprime en la pantalla "CORRECTO"
            cp+=1
            sonido_acierto()
            celebrate(d, my_servo, 3)  # Celebrar durante 3 segundos y mueve el servo
            time.sleep(3)
            
            ledb.on()
            ledi.off()
            assign_random_number()
        elif rojo==True or verde==True:
            print("Incorrecto")
            d.home()
            d.clear()
            d.write('Incorrecto :(')  # imprime en la pantalla "INCORRECTO"
            d.color(255, 255, 0)
            sonido_desacierto()
            time.sleep(3)
            ledb.off()
            ledi.on()
            assign_random_number()
    time.sleep(1)