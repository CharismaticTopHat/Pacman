import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np

#Arreglos en tamaño de Pixeles con Columnas y Filas de la Matriz de Control
Xpx=np.array([0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,16])
Zpx=np.array([0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,16])

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

class Ghost:
    def __init__(self, position, Xindex, Zindex, image_path):
        self.Xindex = Xindex
        self.Zindex = Zindex
        self.position = position
        self.actualX = Xpx[self.Xindex]
        self.actualZ = Zpx[self.Zindex]
        self.direction = [0, 0, 0]  # Dirección inicial
        self.distance_counter = 25  # Contador de distancia recorrida en la dirección actual
        self.sprite = self.load_texture(image_path)

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

    def update(self):
        # Si el contador alcanza 25 píxeles, cambia la dirección
        if self.distance_counter >= 32.5:
            valor = controlMatrix[self.actualZ][self.actualX]
            print(self.actualZ)
            print(self.actualX)
            print(valor)
            print(self.direction)

            if valor == 11:
                directions = [[0, 0, 1]]
            elif valor == 12:
                directions = [[0, 0, -1]]
            elif valor == 13:
                directions = [[1, 0, 0]]
            elif valor == 14:
                directions = [[-1, 0, 0]]
            elif valor == 15:
                directions = [[0, 0, -1], [0, 0, 1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 16:
                directions = [[-1, 0, 0], [1, 0, 0]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 17:
                directions = [[1, 0, 0], [0, 0, 1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 18:
                directions = [[1, 0, 0], [0, 0, -1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 19:
                directions = [[-1, 0, 0], [0, 0, 1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 20:
                directions = [[-1, 0, 0], [0, 0, -1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 21:
                directions = [[-1, 0, 0], [1, 0, 0], [0, 0, 1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 22:
                directions = [[-1, 0, 0], [1, 0, 0], [0, 0, -1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 23:
                directions = [[1, 0, 0], [0, 0, -1], [0, 0, 1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 24:
                directions = [[-1, 0, 0], [0, 0, -1], [0, 0, 1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 25:
                directions = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1]]
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            elif valor == 26:
                directions = []
                opposite_direction = [-x for x in self.direction]
                if opposite_direction in directions:
                    directions.remove(opposite_direction)
            else:
                directions = [self.direction]
            # Direcciones posibles: DERECHA, IZQUIERDA, ABAJO, ARRIBA
            # Seleccionar una dirección aleatoria
            self.direction = random.choice(directions)
            # Reiniciar el contador
            self.distance_counter = 0

            #Asignacion de columnas y renglones
            if self.direction == [-1, 0, 0]:
                print("derecha")
                self.Xindex += 25
                self.actualX = Xpx[self.Xindex]

            elif self.direction == [1, 0, 0]:
                print("izquierda")
                self.Xindex -= 25
                self.actualX = Xpx[self.Xindex]

            elif self.direction == [0, 0, 1]:
                print("arriba")
                self.Zindex -= 25
                self.actualZ = Zpx[self.Zindex]

            elif self.direction == [0, 0, -1]:
                print("abajo")
                self.Zindex += 25
                self.actualZ = Zpx[self.Zindex]
        # Actualizar la posición del fantasma según la dirección y la velocidad
        self.position[0] += self.direction[0]/3.5
        self.position[2] += self.direction[2]/3.46
        self.distance_counter += 1

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