from madison_axi.axi import *
from random import *

initialize()
pen_up()
move_to(0,0)
point_in_direction(0)
pen_down()

def squiral(length):
    for length in range(randrange(1,250)):
        move_forward(2 * length)
        turn_right(90)

pen_up()
move_to(0,0)
point_in_direction(0)
pen_down()

def triral(length):
    for length in range(randrange(1,250)):
        move_forward(2 * length)
        turn_right(120)
        
squiral(50)
triral(50)

pen_up()
cleanup()
