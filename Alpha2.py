import pygame
from pygame.locals import *
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen = pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Penguine")

def init():
    gl.glClearColor(1.0, 1.0, 1.0, 1)
    glu.gluOrtho2D(-800, 800, -800, 800)

def circle(rx, ry, x, y, startangle=0, endangle=360):
    PI = 3.1416
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(x, y)
    angle = startangle
    while angle <= endangle:
        rangle = PI * angle / 180.0
        gl.glVertex2f(x + (math.cos(rangle) * rx), y + (math.sin(rangle) * ry))
        angle += 2.0 * PI / 1000.0
    gl.glEnd()

def draw_shapes():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glColor3f(1, 1.0 / 255 * 182.0, 1.0 / 255 * 12.0)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(-50, 50)
    gl.glVertex2f(-300, -50)
    gl.glVertex2f(-80, -50)
    gl.glEnd()

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(50, 50)
    gl.glVertex2f(300, -50)
    gl.glVertex2f(80, -50)
    gl.glEnd()

    gl.glColor3f(0, 0, 0)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(-150, 350)
    gl.glVertex2f(-400, 250)
    gl.glVertex2f(-180, 250)
    gl.glEnd()

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(150, 350)
    gl.glVertex2f(400, 250)
    gl.glVertex2f(180, 250)
    gl.glEnd()

    circle(200, 150, 0, 400, 0, 360)
    circle(300, 250, 0, 150, 0, 180)
    circle(300, 150, 0, 150, 180, 360)

    circle(20, 20, -60, 400, 0, 360)
    circle(20, 20, 60, 400, 0, 360)

    gl.glColor3f(1, 1, 1)
    circle(80, 80, -60, 400, 0, 360)
    circle(20, 20, -60, 400, 0, 360)
    circle(80, 80, 60, 400, 0, 360)
    circle(250, 200, 0, 150, 0, 180)
    circle(250, 120, 0, 150, 180, 360)

    gl.glColor3f(0, 0, 0)
    circle(20, 20, -60, 400, 0, 360)
    circle(20, 20, 60, 400, 0, 360)
    circle(5, 5, -60, 400, 0, 360)
    circle(5, 5, 60, 400, 0, 360)

    gl.glColor3f(1, 1, 1)
    circle(5, 5, -60, 400, 0, 360)
    circle(5, 5, 60, 400, 0, 360)

    gl.glColor3f(1, 1.0 / 255 * 182.0, 1.0 / 255 * 12.0)
    circle(60, 60, 0, 320, 60, 120)

    gl.glFlush()

def main():
    init()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_shapes()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()