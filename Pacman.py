import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np

#Arreglos en tamaño de Pixeles con Columnas y Filas de la Matriz de Control
Xpx=np.array([0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 16])
Zpx=np.array([0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 16])

controlMatrix = [[20,0,22,0,0,0,22,13,0,14,22,0,0,0,22,0,18],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [11,0,24,0,18,0,19,0,22,0,17,0,20,0,23,0,11],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [12,0,0,0,0,0,20,0,21,0,18,0,0,0,0,0,12],
                    [24,0,23,0,0,0,0,0,0,0,0,0,0,0,24,0,23],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,11,0,24,0,17,0,0,0,19,0,23,0,11,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,12,0,24,0,18,0,0,0,20,0,23,0,12,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [24,0,23,0,0,0,0,0,0,0,0,0,0,0,24,0,23],
                    [11,0,0,0,0,0,19,0,22,0,17,0,0,0,0,0,11],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [12,0,24,0,17,0,20,0,21,0,18,0,19,0,23,0,12],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [19,0,21,0,0,0,21,13,0,14,21,0,0,0,21,0,17]]


import random

class Pacman:
    def __init__(self, position, Xindex, Zindex, image_path):
        self.Xindex = Xindex
        self.Zindex = Zindex
        self.position = position
        self.actualX = Xpx[self.Xindex]
        self.actualZ = Zpx[self.Zindex]
        self.direction = [0, 0, 0]
        self.distance_counter = 0
        self.sprite = self.load_texture(image_path)
        self.control = 0
        self.valor = 0
        self.temp_directions = [0, 0, 0]
        self.cont = 0

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glBindTexture(GL_TEXTURE_2D, self.sprite)
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)  # Usa color blanco para mostrar correctamente la textura

        glBegin(GL_QUADS)
        size = 8  # The size of the Pac-Man texture in the world space
        glTexCoord2f(0, 0); glVertex3f(0, 0, 0)  # Inferior izquierda
        glTexCoord2f(1, 0); glVertex3f(size, 0, 0)  # Inferior derecha
        glTexCoord2f(1, 1); glVertex3f(size, 0, size)  # Superior derecha
        glTexCoord2f(0, 1); glVertex3f(0, 0, size)  # Superior izquierda
        glEnd()

        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def update(self, direction):
        row = self.actualZ
        col = self.actualX
        previus = self.direction

        if row != -1 and col != -1:
            self.direction = direction
            self.valor = controlMatrix[self.actualZ][self.actualX]
            print(self.valor)

        if self.valor == 11:
            directions = [[0, 0, 1]]
        elif self.valor == 12:
            directions = [[0, 0, -1]]
        elif self.valor == 13:
            directions = [[1, 0, 0]]
        elif self.valor == 14:
            directions = [[-1, 0, 0]]
        elif self.valor == 15:
            directions = [[0, 0, -1], [0, 0, 1]]
        elif self.valor == 16:
            directions = [[-1, 0, 0], [1, 0, 0]]
        elif self.valor == 17:
            directions = [[1, 0, 0], [0, 0, 1]]
        elif self.valor == 18:
            directions = [[1, 0, 0], [0, 0, -1]]
        elif self.valor == 19:
            directions = [[-1, 0, 0], [0, 0, 1]]
        elif self.valor == 20:
            directions = [[-1, 0, 0], [0, 0, -1]]
        elif self.valor == 21:
            directions = [[-1, 0, 0], [1, 0, 0], [0, 0, 1]]
        elif self.valor == 22:
            directions = [[-1, 0, 0], [1, 0, 0], [0, 0, -1]]
        elif self.valor == 23:
            directions = [[1, 0, 0], [0, 0, -1], [0, 0, 1]]
        elif self.valor == 24:
            directions = [[-1, 0, 0], [0, 0, -1], [0, 0, 1]]
        elif self.valor == 25:
            directions = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]]
        elif self.valor == 26:
            directions = []
        elif self.valor == 0:
            directions = [previus, previus * -1]

        else:
            directions = []


        # Verificar si self.direction está en las direcciones permitidas
        if self.direction not in directions and self.valor != 0:
            self.direction = [0, 0, 0]
        elif self.direction not in directions and self.valor == 0 and self.cont == 0:
            self.temp_directions = directions
            self.cont += 1
            self.direction = [0, 0, 0]
        elif self.direction not in self.temp_directions and self.valor == 0 and self.cont == 1:
            self.direction = [0, 0, 0]
        elif self.direction in self.temp_directions and self.valor == 0 and self.cont == 1:
            self.cont = 0
            self.temp_directions = [0, 0, 0]


        if self.direction == [-1, 0, 0]:
            self.Xindex += 1
            self.actualX = Xpx[self.Xindex]
            self.position[0] += self.direction[0] / 3.5

        if self.direction == [1, 0, 0]:
            self.Xindex -= 1
            self.actualX = Xpx[self.Xindex]
            self.position[0] += self.direction[0] / 3.5

        if self.direction == [0, 0, 1]:
            self.Zindex -= 1
            self.actualZ = Zpx[self.Zindex]
            self.position[2] += self.direction[2] / 3.46

        if self.direction == [0, 0, -1]:
            self.Zindex += 1
            self.actualZ = Zpx[self.Zindex]
            self.position[2] += self.direction[2] / 3.46

        print(f"Row: {self.actualZ}")
        print(f"Colum: {self.actualX}")

    @staticmethod
    def load_texture(image_path):
        image = pygame.image.load(image_path)
        image_data = pygame.image.tostring(image, "RGBA", 1)
        width, height = image.get_size()

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        return texture_id