#app
from p5 import *
from classes.clases import *
from models.models import *

MAX_WIDTH = 800
MAX_HEIGHT = 700
ventana = None

def setup():
    global ventana
    size(MAX_WIDTH, MAX_HEIGHT)
    ventana = Ventana()

def draw():
    background(220)
    ventana.dibujar()


run()