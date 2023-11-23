#Código para el funcionamiento de elegir un elemento al azar en el prototipo
impoert random
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