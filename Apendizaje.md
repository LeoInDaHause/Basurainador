# Proceso de Aprendizaje

1. en un principio al empezar con el microcontrolador se empezo por una raspberry pi pico, en este proceso mediante un computador se utilizaron librerias que funcionaran para el Programa de programacion en este caso el usado fue Thonny.

![se empieza la configuración de la raspberry](https://github.com/LeoInDaHause/Basurainador/assets/145580263/c979784a-77c5-47b1-9be0-c0d03916c9ff)

los problemas que se tubieron con la raspberry pi pico:

en este desarrollo se experimentaron diferentes problemas, debido a que se tubo que instalar diferentes archivos, y pedir permisos al computador para poderlos ejecutar, ya teniendo la rasbperry pi pico conectada al computador y a Thonny se empezo a cacharrear el funcionamiento con los pines mediante actividades durante el taller. nos guiamos mediante el datacheet y de diferentes paginas encontradas en internet, la inmensa mayoria en ingles.

![se enciende el sensor con la raspberry](https://github.com/LeoInDaHause/Basurainador/assets/145580263/f92ea0a6-6f2d-4c82-b09b-5d995e3a37b9)
![se empieza a cacharrearle al sensor TCS3200, con la raspberry](https://github.com/LeoInDaHause/Basurainador/assets/145580263/f9468f3b-2b10-4851-8b52-e5cb527eaa0d)


Otro problema presentado fue a partir de intentar conectar los pines con los diferentes componentes en la protoboard, este problema se presentaba a razon de que no habia una buena conexion en la protoboard, lo que conllevaba a que aveces funcionaba y aveces no. En consecuencia de esto se decide soldar a los pines de la raspberry pi pico unas regletas, para poner conectar estas con jumpers hembra, debido a la inexperiencia la soldadura quedo mal, y la raspberry pi pico presento otros problemas 

![pines soldados pico](https://github.com/LeoInDaHause/Basurainador/assets/145580263/6f64840f-95db-45ec-b8b6-1bc1cc80af8f)


despues de presentar los problemas anteriormente mencionado, se decidio en conjunto utilizar el microcontrolador ESP32, esto debido a que por una parte ya tiene las regletas soldadas, tambien porque esta mejor documentado por internet que la rasbperry pi pico, y ademas ya tiene mas bibliotecas.


2. comienza el proceso de (configurar) la ESP32 con el computador y con micropython,

![ESP32 configuración](https://github.com/LeoInDaHause/Basurainador/assets/145580263/6b5ed483-dd46-4216-bff7-e1a90f6b4b46)

3. ya configurado la ESP32, se empieza a revisar los pines para realizar las conexiones, para esto se utilizo una Guia

![image](https://github.com/LeoInDaHause/Basurainador/assets/145580263/be578ef2-7340-49ef-827c-907fe42bb89f)

4. Cuando se configuro la ESP32 con el Sensor TCS3200, se empezo a detectar un problema que en un principo no sabiamos su causa, este problema se trataba sobre los valores que arrojaba la TCS3200 cuando se intentaba determinar un color, debido a que eran valores que variaban a cada segundo y de una manera aleatoria, (paralelo a esto tambien exisatian errores de programación)
esto de detecto cuando se reviso lo que sucedia en el osciloscopio.
La razón de este problema era debido al ruido que habia habia en el ambiente (luz natural o luz de los bombillos)
por lo cual nos dimos de cuenta de que para que el sensor funcione correctamente este debia de estar en cierta oscuridad, por lo que nuestro proyecto debe de estar en lugares cerrados.

![image](https://github.com/LeoInDaHause/Basurainador/assets/145580263/f8fa7fb0-5a03-4483-8f1f-75cc281547f0)

Cuando se consiguio solucionar los problemas tanto de programacion como de iluminación, se prosiguio a hacer el servomotor

5. Empiza la configuracion del servomotor

https://github.com/LeoInDaHause/Basurainador/assets/145580263/3488bf7d-7020-4524-8e29-eb3a34d98795

ya configurado correctamente el servomotor se prosigue

6. Configuracion de la Pantalla LCD

con la pantalla LCD se tubo un problema con respecto a su conexion en un principio debido a que se necesitaba un cable especial que no se pudo conseguir, por lo que se tubo que soldar.

(imagen)

7. ya soldada los cables a la pantalla lcd se empiza a relaizar la programacion para que esta proyectara lo que queriamos, en este caso producir un mensaje aleatorio solicitandole al usuario un elemento(basura) entre ("Organico", "Papel y Metal", "Plastico y Vidrio"), y dependiendo de si es correcto esta daria un mensaje "Correcto" y en otro caso "Incorrecto"

https://github.com/LeoInDaHause/Basurainador/assets/145580263/93dd53f0-decb-44f5-940f-e1c6dde341c4
