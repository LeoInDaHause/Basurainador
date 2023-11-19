cuando se configuro la ESP32 con el Sensor TCS3200, se empezo a detectar un problema que en un principo no sabiamos su causa, 
este problema se trataba sobre los valores que arrojaba la TCS3200 cuando se intentaba determinar un color, debido a que 
eran valores que variaban a cada segundo y de una manera aleatoria, (paralelo a esto tambien exisatian errores de programación, que el profesor nos fue ayudando a ir resolviendo este problema)
esto de detecto cuando se reviso lo que sucedia en el osciloscopio.
La razón de este problema era debido al ruido que habia habia en el ambiente (luz natural o luz de los bombillos)
por lo cual nos dimos de cuenta de que para que el sensor funcione correctamente este debia de estar en cierta oscuridad, 
por lo que nuestro proyecto debe de estar en lugares cerrados.

![image](https://github.com/LeoInDaHause/Basurainador/assets/145580263/4159c595-fd48-48c5-8b2b-b2c478388036)


Cuando se consiguio solucionar los problemas tanto de programacion como de iluminación, se prosiguio a hacer el servomotor
