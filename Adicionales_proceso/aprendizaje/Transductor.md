Al comienzo del proceso teniamos pensado poner un parlante pequeño que trasmitiera sonidos a partir de si el elemento era correcto o no, a lo largo del proceso este objetivo quedo
al final, por lo cual la ultima semana, empezamos a cacharrear con el parlante. pero hubo un problema.

resulta que cuando poniamos el parlante en el proyecto, junto a los otros componentes, pensabamos que este como que consumia mayor voltaje haciendo que el servomotor se volviera loco y perdieramos
el control de este. por lo cual habiamos desistido debido a que ya teniamos el tiempo sobre el cuello, pero un dia antes de la presentacion, se detecto de que trataba el error.

este error se producia por un PIN

este fue por que usamos un PIN que ya estaba definido en el codigo, produciendo una mala señal y comprometiendo el servomotor
ya despues, detectado este error, se corrigio, por lo que al final nos quedamos con el PIN PWM (señal que genera al parlante para que reproduzca el sonido)




