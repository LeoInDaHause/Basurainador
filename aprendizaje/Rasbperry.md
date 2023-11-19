en un principio al empezar con el microcontrolador se empezo por una raspberry pi pico, en este proceso mediante un 
computador se utilizaron librerias que funcionaran para el Programa de programacion en este caso el usado fue Thonny.

![se empieza la configuración de la raspberry](https://github.com/LeoInDaHause/Basurainador/assets/145580263/c979784a-77c5-47b1-9be0-c0d03916c9ff)

los problemas que se tubieron con la raspberry pi pico:

en este desarrollo se experimentaron diferentes problemas, debido a que se tubo que instalar diferentes archivos, 
y pedir permisos al computador para poderlos ejecutar, ya teniendo la rasbperry pi pico conectada al computador y 
a Thonny se empezo a cacharrear el funcionamiento con los pines mediante actividades durante el taller. nos guiamos
mediante el datacheet y de diferentes paginas encontradas en internet, la inmensa mayoria en ingles.

![se enciende el sensor con la raspberry](https://github.com/LeoInDaHause/Basurainador/assets/145580263/f92ea0a6-6f2d-4c82-b09b-5d995e3a37b9)
![se empieza a cacharrearle al sensor TCS3200, con la raspberry](https://github.com/LeoInDaHause/Basurainador/assets/145580263/f9468f3b-2b10-4851-8b52-e5cb527eaa0d)


Otro problema presentado fue a partir de intentar conectar los pines con los diferentes componentes en la protoboard, 
este problema se presentaba a razon de que no habia una buena conexion en la protoboard, lo que conllevaba a que 
aveces funcionaba y aveces no. En consecuencia de esto se decide soldar a los pines de la raspberry pi pico unas regletas, 
para poner conectar estas con jumpers hembra, debido a la inexperiencia la soldadura quedo mal, y la 
raspberry pi pico presento otros problemas 

![pines soldados pico](https://github.com/LeoInDaHause/Basurainador/assets/145580263/6f64840f-95db-45ec-b8b6-1bc1cc80af8f)


despues de presentar los problemas anteriormente mencionado, se decidio en conjunto utilizar el microcontrolador ESP32, 
esto debido a que por una parte ya tiene las regletas soldadas, tambien porque esta mejor documentado por internet que 
la rasbperry pi pico, y ademas ya tiene mas bibliotecas
