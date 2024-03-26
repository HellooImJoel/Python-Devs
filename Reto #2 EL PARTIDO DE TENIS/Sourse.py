# EL PARTIDO DE TENIS



POINTS = ("Love", "15", "30", "40", "Deuce", "Ventaja")


def imprimirPuntuaciones(pointsP1, pointsP2):
    limit = 4
    if pointsP1 == limit and pointsP2 == limit:
        print("Deuce")

    elif pointsP1 >= limit or pointsP2 >= limit:
        puntos = pointsP1 - pointsP2
        if puntos == 0:
            print("Deuce")
        elif puntos == 1:
            print("Ventaja P1")
        elif puntos == -1:
            print("Ventaja P2")
        elif puntos >= 2:
            print("Ha ganado el P1")
            return
        else:
            print("Ha ganado el P2")
            return
            

    else:
        print(f"{POINTS[pointsP1]} - {POINTS[pointsP2]}")



pointsP1 = 0
pointsP2 = 0
def anotador(equipo):
    global pointsP1, pointsP2
    if(equipo == 'P1'):
        pointsP1 += 1
    elif equipo == 'P2':
        pointsP2 += 1

    imprimirPuntuaciones(pointsP1, pointsP2)
    

def main():
    game = ['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P2']
    for secuencia in game:
        anotador(secuencia)


if __name__ == '__main__':
    main()


