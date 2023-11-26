#Código para la asignación y clasificación de los colores por medio de ranjos del sensor TCS3200
    if rgb[0]>10 and rgb[0]>rgb[1] and rgb[0]>rgb[2]:
        rojo=True
        verde=False
        azul=False
        print('Rojo')
    if rgb[2]>10 and rgb[2]>rgb[1] and rgb[2]>rgb[0]:
        verde=False
        azul=True
        rojo=False
        print('Azul')
    if rgb[1]>20 and rgb[1]>rgb[0] and rgb[1]>rgb[2]:
        verde=True
        azul=False
        rojo=False
        print('Verde')