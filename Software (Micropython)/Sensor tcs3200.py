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