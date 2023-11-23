#Codigo para el manejo del servomotor en el prototipo
from servo import Servo
from machine import Pin
import time
my_servo = Servo(pin_id=14)
my_servo.write(127)
my_servo.write(210)
my_servo.write(127)