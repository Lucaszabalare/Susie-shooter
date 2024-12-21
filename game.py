# Creating the library
import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 450

TITLE = "Susie"
# Variable to hold messages
msg = ""

# Creating the sprite
susie = Actor("susie")

def draw():
    screen.clear()
    screen.fill(color = "white")
    susie.draw()
    screen.draw.text(msg,center = (300,20),fontsize = 30,color = "orange")

def susie_place():
    susie.x = randint(50,450)
    susie.y = randint(50,400)

def on_mouse_down(pos):
    global msg
    if susie.collidepoint(pos):
        msg = "Susie shot!"
        susie_place()
    else:
        msg = "Susie missed!"

susie_place()
pgzrun.go()