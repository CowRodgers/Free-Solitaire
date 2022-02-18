from turtle import Screen, Turtle
import time
from random import choice

# This programme provides an entirely random autoplay solitary game
# We use the module turtle to display the game

ALIGNMENT = "center"
FONT = "Stencil"
TEXT_SIZE = 40
TEXT_ASPECT = "bold"

screen = Screen()
screen.screensize(620, 620)
screen.title("FREE SOLITAIRE")
screen.bgcolor('green')


def playground():
    """affichage du plateau de jeu dans un fenêtre turtle,
    puis crée et positionne les pions,
    puis retourne ces coordonnées, la liste des pions créés et les coordonnées libres"""
    screen.bgcolor('green')
    screen.tracer(0)
    liner = Turtle()
    liner.hideturtle()
    liner.penup()
    liner.goto(-150, 300)
    liner.pendown()
    liner.color('black', 'yellow')
    liner.begin_fill()
    liner.pendown()
    for shape in range(4):
        liner.forward(300)
        liner.right(90)
        liner.forward(150)
        liner.left(90)
        liner.forward(150)
        liner.right(90)
    liner.end_fill()

    """liste toutes les coordonnées initiales des pions disponibles"""
    coordinates = []
    coordinates = [(-75, 75), (75, 75), (75, -75), (-75, -75),
                   (-75, 150), (75, 150), (75, -150), (-75, -150),
                   (-150, 75), (150, 75), (150, -75), (-150, -75),
                   (0, 75), (0, -75), (-75, 0), (75, 0),
                   (0, 150), (0, -150), (-150, 0), (150, 0),
                   (0, 225), (0, -225), (225, 0), (-225, 0),
                   (-75, 225), (-75, -225), (225, -75), (-225, 75),
                   (75, 225), (-225, -75), (225, 75), (75, -225)]

    """création des pions avec Turtle"""
    pions = []
    for coordo in coordinates:
        pion = Turtle()
        pion.hideturtle()
        pion.shape('circle')
        pion.penup()
        pion.color('green')
        pion.shapesize(2)
        pion.setpos(coordo)
        pion.showturtle()
        pions.append(pion)

    free_coordinates = []
    free_coordinates = [(0, 0)]

    screen.tracer(1)
    return [coordinates, pions, free_coordinates]


def game(coordinates, pions, free_coordinates):
    """joue le jeu tant que des coordonnées des pions sont disponibles"""
    time.sleep(2.5)
    start_time = time.time()

    while len(coordinates) > 1:
        jump_from = []
        free_spot = choice(free_coordinates)
        """sélectionne une case libre du plateau"""
        (x, y) = (free_spot[0], free_spot[1])
        pairs_coordo_list = [
            [((x + 150), y), ((x + 75), y)],
            [((x - 150), y), ((x - 75), y)],
            [(x, (y + 150)), (x, (y + 75))],
            [(x, (y - 150)), (x, (y - 75))]
        ]
        end_time = time.time()
        # print(end_time - start_time)
        if end_time - start_time >= 34:
            """sort de la boucle après 34 secondes de jeu"""
            break
        for coordos in pairs_coordo_list:
            if coordos[0] in coordinates and coordos[1] in coordinates:
                """enclenche le saut si un pion est disponible pour se déplacer sur la case libre choisie"""
                jump_from.append(coordos)
        if not jump_from:
            continue
        jump_and_remove_pions = choice(jump_from)
        coord_jumper_pion = jump_and_remove_pions[0]
        coord_pion_to_remove = jump_and_remove_pions[1]

        time.sleep(0.3)
        for pion in pions:
            if pion.position() == coord_jumper_pion:
                pion.dot(20, 'pink')
                pion.goto(free_spot)

        """mise à jour des listes des pions et des cases libres (coordonnées) après le saut"""
        free_coordinates.remove(free_spot)
        coordinates.append(free_spot)
        free_coordinates.append(coord_jumper_pion)
        coordinates.remove(coord_jumper_pion)

        time.sleep(0.3)
        for pion in pions:
            if pion.position() == coord_pion_to_remove:
                pion.hideturtle()
                pion.dot(20, 'pink')
                pions.remove(pion)
        free_coordinates.append(coord_pion_to_remove)
        coordinates.remove(coord_pion_to_remove)

        """cas très peu probable d'un jeu gagnant, provoque l'affichage gagnant puis stop le jeu"""
        if len(coordinates) == 1:
            winner = Turtle()
            winner.penup()
            winner.hideturtle()
            winner.color('red')
            winner.goto(0, -32)
            winner.write('Finally, the ROBOT win !', False, ALIGNMENT, (FONT, TEXT_SIZE, TEXT_ASPECT))
            play = False
            return play


play = True
"""lance le jeu"""
while play:
    screen.clearscreen()
    lists = playground()
    if game(lists[0], lists[1], lists[2]) == False:
        break

screen.exitonclick()
