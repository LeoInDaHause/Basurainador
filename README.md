# Basurainador
Proyecto Electrónica - 1 Semestre

## BASURA-INADOR
un proyecto que tiene como objetivo centra crear una cultura positiva alrededor de las basuras, en esto se trata sobre el reciclaje y el manejo de las basuras. con el objetivo de lograr esto se crea un "artefacto" que sea didactico y que llame la atención de niños entre los 5 a 7 años.

para lograr construir este proyecto "artefacto", se a realizado una investigación previa, alrededor de la cultura y de como contruir esta cultura en los niños. y tambien se realizo una investigación sobre los materiales para usar, y de la manera mas eficiente de conseguir este artefacto.

las concluciones obtenidas de estas investigaciones son:

1. por parte de lo cultural, se identifico que la mejor manera de crear una cultura en los niños eran son estimulos que a estos les llamara la atencion, por ejemplo luces y sonidos

2. a partir de la investigación realizada para temas de material y eficiencia del proyecto, de decide el uso de un microcontrolador, junto a un sensor de color, luces led, y sonidos.

   (en un principio se tenia la idea de realizar 3 canecas de basura que tubieran el objetivo de separar las basuras, en organicos, papel y carton, y metales y vidrios. A medida que fue avanzando el tiempo el proyecto cada vez era mas pulido. hasta el punto en el que unicamente se utilizaria una caneca, y a partir de esto, mediante una pantalla(lcd o oled), se le pidiera al usuario ingresear un tipo de basura, mediante un sensor (TCS3200) detectaria el color de la basura y determinaria, mediante un programa desde el microcontrolador (ESP32), si este elemento es el solicitado o no. en caso de que el elemento fuera correcto, este arrojaria la LUZ del elemento y produciria un sonido "positivo", y habriria la tapa de la caneca, en caso contrario este arrojaria una LUZ diferente al elemento y produciria un sonido "malo", y la tapa no habriria.  )

de esta manera se espera que el niño de 5 a 7 años interactue con el "artefacto" sin aburrirse, y genernado en este la cultura deseada, para solucionar una problematica que se vive en la actualidad y que tiene graves consecuencias, como lo es el impacto a la salud, clima, biodiversidad, suciedad, entre otras cosas.

## Diagrama de Caja negra
<img width="890" alt="image" src="https://github.com/LeoInDaHause/Basurainador/assets/145580263/44824039-855c-4b29-b5df-d9eacd21b228">

## Diagrama de Tecnologico

![Basurainado diagrama refinado_page-0001](https://github.com/LeoInDaHause/Basurainador/assets/145580263/1e3c38ab-1e7f-4c89-8f65-5467335ea5b1)

## Póster

![Plantilla_TPI pptx](https://github.com/LeoInDaHause/Basurainador/assets/145580263/4bc3f24f-2540-4486-b662-999ec0575961)

# Elementos usados para la construcción del "Artefacto"
## PCB:
(falta porner imagen)
## MICROCONTROLADOR : ESP32
![image](https://github.com/LeoInDaHause/Basurainador/assets/145580263/1132f75d-44ca-4851-b980-5a268a7b3840)
## SENSOR: TCS3200
![image](https://github.com/LeoInDaHause/Basurainador/assets/145580263/349dfbfd-b36b-4805-aa15-5b5d4be5e8ec)
## Leds: color: Azul. Verde. Rojo. Amarillo
![image](https://github.com/LeoInDaHause/Basurainador/assets/145580263/4c750721-732a-460f-a701-f75083fb33bf)
## Pantalla: aun falta definir (LCD ó OLED)
(falta poner imagen)
## material usado para la contruccion de la caneca: madera MDF (fibras de densidad media)
<img width="233" alt="image" src="https://github.com/LeoInDaHause/Basurainador/assets/145580263/7f518f0e-8650-4f9f-b3a6-8981b6134db7">



# Proceso de aprendizaje:
1. en un principio al empezar con el microcontrolador se empezo por una raspberry pi pico, en este proceso mediante un computador se utilizaron librerias que funcionaran para el Programa de programacion en este caso el usado fue Thonny.

   
![se empieza la configuración de la raspberry](https://github.com/LeoInDaHause/Basurainador/assets/145580263/c979784a-77c5-47b1-9be0-c0d03916c9ff)


