#app.py
from p5 import *
from classes.clases import *
from patron.Builders import Builder
import random

figuras = []

MAX_WIDTH = 800
MAX_HEIGHT = 700
NUM_FIGURAS = 15          # <-- número para más o menos figuras

COLORES_RELLENO = [
    "#463932", "#12B85D", "#E84393", "#F5A623",
    "#4A90E2", "#9B59B6", "#E74C3C", "#1ABC9C",
    "#F39C12", "#2ECC71"
]

COLORES_BORDE = [
    "#000000", "#FFFFFF", "#333333", "#FF0000",
    "#0000FF", "#222222"
]


def setup():
    global MAX_WIDTH, MAX_HEIGHT
    size(MAX_WIDTH, MAX_HEIGHT)
    generarFiguras()


def draw():
    background(220)
    for figura in figuras:
        interactuarFig(figura)


def interactuarFig(figura: Figura):
    figura.dibujar()
    figura.desplazar_rebotar(max_x=MAX_WIDTH, max_y=MAX_HEIGHT)


def crearFiguraAleatoria():
    tipo        = random.randint(0, 1)                          # 0 = cuadrado, 1 = elipse
    x           = random.uniform(0, MAX_WIDTH  - 60)
    y           = random.uniform(0, MAX_HEIGHT - 60)
    tamano      = random.randint(30, 90)   # mismo valor → cuadrado y círculo perfectos
    ancho       = tamano
    alto        = tamano
    grosor      = random.randint(1, 5)
    color_fill  = random.choice(COLORES_RELLENO)
    color_borde = random.choice(COLORES_BORDE)

    builder = (Builder()
               .configBorde(grosor, color_borde)
               .configColor(color_fill)
               .configDimension(ancho, alto)
               .configPosicion(x, y))

    if tipo == 1:
        builder = builder.esElipse()

    figura = builder.build()

    # velocidades aleatorias (positivas o negativas)
    figura.vel_x = random.choice([-1, 1]) * random.uniform(1.5, 4.5)
    figura.vel_y = random.choice([-1, 1]) * random.uniform(1.5, 4.5)

    return figura


def generarFiguras():
    for _ in range(NUM_FIGURAS):
        figuras.append(crearFiguraAleatoria())


run()