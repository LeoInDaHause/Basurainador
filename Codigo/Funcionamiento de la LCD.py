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