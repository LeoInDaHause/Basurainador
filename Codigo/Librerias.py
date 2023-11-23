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