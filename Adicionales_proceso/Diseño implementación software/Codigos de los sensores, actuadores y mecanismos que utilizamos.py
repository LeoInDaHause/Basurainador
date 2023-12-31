# LIBRERIAS

 # esta libreria se utiliza para el sensor TCS3200, para que capte bien los colores RGB
from tcs3200 import TCS3200
# esta libreria se utiliza para manejar la pantalla LCD de 4 pines  #16 por fila y 2 columnas
import i2c_lcd
# esta libreria es para manejar el servomotor SG90
from servo import Servo
# esta libreria se utiliza para definir los pines de la ESP32 relacionarlos con la LCD
from machine import Pin, I2C
# tiempo
import time
# tiempo en microsegundo
import utime
# Manejar cosas del sensor
from neopixel import NeoPixel
# Random
import random

#Codigo Para el manejo del sensor de color TCS3200:
from tcs3200 import TCS3200 
from neopixel import NeoPixel
tcs3200 = TCS3200(OUT=19, S2=5, S3=18, S0=17, S1=33, LED=10)
tcs3200.debugging=tcs3200.ON
tcs3200.led = tcs3200.ON
NEOPIXEL_PIN=26
NO_OF_LEDS=7

neoPixel = NeoPixel(Pin(NEOPIXEL_PIN),NO_OF_LEDS)
tcs3200.freq_divider = tcs3200.TWO_PERCENT

black_freq = [2890.257, 2601.051, 3495.77, 9454.477]
white_freq = [15283.51, 15494.27, 14985.76, 11150.76]
tcs3200.calibrateSet(black_freq,white_freq)

rgb = tcs3200.rgb
for i in range(NO_OF_LEDS):
    neoPixel[i] = (rgb[0],rgb[1],rgb[2])
neoPixel.write()

#Código para la LCD y su funcionamiento en el prototipo
import i2c_lcd #16 por fila y 2 columnas
from machine import Pin, I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
d = i2c_lcd.Display(i2c, lcd_addr=0x3e, rgb_addr=0x62)
d.home()
d.clear()

def color():
    for i in range(2):
        d.color(0, 0, 255)  # Azul
        time.sleep(0.5)
        d.color(0, 255, 0)  # Verde
        time.sleep(0.5)
        d.color(255, 0, 0)  # Rojo
        time.sleep(0.5)
    d.color(128, 128, 128)

d.write('Ingrese Papel')

#Código para la asignación y clasificación de los colores por medio de ranjos del sensor TCS3200
    if rgb[0]>10 and rgb[0]>rgb[1] and rgb[0]>rgb[2]:
        rojo=True
        verde=False
        azul=False
        print('Rojo')
    if rgb[2]>10 and rgb[2]>rgb[1] and rgb[2]>rgb[0]:
        verde=False
        azul=True
        rojo=False
        print('Azul')
    if rgb[1]>20 and rgb[1]>rgb[0] and rgb[1]>rgb[2]:
        verde=True
        azul=False
        rojo=False
        print('Verde')

#Código para el funcionamiento de elegir un elemento al azar en el prototipo
import random
def assign_random_number():
    global P, O, M, rojo, verde, azul
    numero = random.randint(1, 3)
    if numero == 1:
        print('Ingrese un elemento papel o cartón')
        d.home()
        d.clear()
        d.write('Ingrese Papel')
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
        d.write('Ingrese Organico')
        color()
        P=False
        O=True
        M=False
        rojo=False
        verde=False
        azul=False
    else:
        print('Ingrese un elemento plástico, metal o vidrio')
        d.home()
        d.clear()
        d.write('Ingrese Plastico')
        color()
        P=False
        O=False
        M=True
        rojo=False
        verde=False
        azul=False

assign_random_number()

#Código para encender un led en el prototipo
from machine import Pin

ledr=Pin(15, Pin.OUT)
ledg=Pin(2, Pin.OUT)
ledb=Pin(4, Pin.OUT)
ledi=Pin(23, Pin.OUT)

#Codigo para el manejo del servomotor en el prototipo
from servo import Servo
from machine import Pin
import time
my_servo = Servo(pin_id=14)
my_servo.write(127)
my_servo.write(210)
my_servo.write(127)

#Proceso para que el elemento identifique el color correcto e incorrecto:
    if O==True:
        if verde==True:
            print("Correcto")
            d.home()
            d.clear()
            d.write('¡Correcto!')
            ledg.on()
            celebrate(d, my_servo, 3)  # Celebrar durante 2 segundos
            time.sleep(1)
            ledr.off()
            ledg.off()
            ledb.off()
            ledi.off()
            assign_random_number()
            
        elif azul==True or rojo==True:
            print("Incorrecto")
            d.home()
            d.clear()
            d.write('Incorrecto :(')
            d.color(255, 255, 0)
            ledi.on()
            time.sleep(3)
            ledr.off()
            ledg.off()
            ledb.off()
            ledi.off()
            assign_random_number()
    if M==True:
        if rojo==True:
            print("Correcto")
            d.home()
            d.clear()
            d.write('¡Correcto!')
            ledr.on()
            celebrate(d, my_servo, 3)  # Celebrar durante 2 segundos
            time.sleep(1)
            ledr.off()
            ledg.off()
            ledb.off()
            ledi.off()
            assign_random_number()
        elif azul==True or verde==True:
            print("Incorrecto")
            d.home()
            d.clear()
            d.write('Incorrecto :(')
            d.color(255, 255, 0)
            ledi.on()
            time.sleep(3)
            ledr.off()
            ledg.off()
            ledb.off()
            ledi.off()
            assign_random_number()
    if P==True:
        if azul==True:
            print("Correcto")
            d.home()
            d.clear()
            d.write('¡Correcto!')
            ledb.on()
            celebrate(d, my_servo, 3)  # Celebrar durante 2 segundos
            time.sleep(3)
            ledr.off()
            ledg.off()
            ledb.off()
            ledi.off()
            assign_random_number()
        elif rojo==True or verde==True:
            print("Incorrecto")
            d.home()
            d.clear()
            d.write('Incorrecto :(')
            d.color(255, 255, 0)
            ledi.on()
            time.sleep(3)
            ledr.off()
            ledg.off()
            ledb.off()
            ledi.off()
            assign_random_number()
    time.sleep(1)
