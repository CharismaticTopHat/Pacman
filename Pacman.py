import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np

#Arreglos en tamaño de Pixeles con Columnas y Filas de la Matriz de Control
Xpx=np.array([0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,16])
Ypx=np.array([0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,16])

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

class Pacman:
        
    def __init__(self, image_path):
        #Se declara la posición de inicio en pixeles en los ejes X y Z
        self.posX=0
        self.posY=0
        #Se inicializa una posicion 0,0 en el tablero
        self.initialPosition = [44,1,27]
        #Velocidad en los 3 ejes
        self.Direction=[]
        self.Direction.append(1)
        self.Direction.append(0)
        self.Direction.append(1)
        #Se inicializa un vector de direccion en torno al eje X
        self.direction = 0
        #Se declaran los movimientos posibles
        self.moves = {
            "Up": False,
            "Right": False,
            "Left": False,
            "Down": False
        }
        #Se declara la velocidad
        self.speed=1
        #Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0]*self.Direction[0] + self.Direction[2]*self.Direction[2])
        self.Direction[0] /= m
        self.Direction[2] /= m
        #Se cambia la maginitud del vector direccion
        self.Direction[0] *= self.speed
        self.Direction[2] *= self.speed
        #Se carga la textura de Pacman
        self.sprite = self.load_texture(image_path)
    
    def availableMoves(self):
        if controlMatrix[self.posX][self.posY] == 0:
            if Xpx[self.posX] == -1:
                self.moves["Right"] = True
                self.moves["Left"] = True
            elif Ypx[self.posY] == -1:
                self.moves["Up"] = True
                self.moves["Down"] = True
        if controlMatrix[self.posX][self.posY] > 0:
            if controlMatrix[self.posX][self.posY] == 11:
                self.moves["Up"] = True
            elif controlMatrix[self.posX][self.posY] == 12:
                self.moves["Down"] = True
            elif controlMatrix[self.posX][self.posY] == 13:
                self.moves["Left"] = True
            elif controlMatrix[self.posX][self.posY] == 17:
                self.moves["Left"] = True
                self.moves["Up"] = True
            elif controlMatrix[self.posX][self.posY] == 19:
                self.moves["Up"] = True
                self.moves["Right"] = True
            elif controlMatrix[self.posX][self.posY] == 21:
                self.moves["Left"] = True
                self.moves["Right"] = True
                self.moves["Up"] = True
            elif controlMatrix[self.posX][self.posY] == 22:
                self.moves["Left"] = True
                self.moves["Right"] = True
                self.moves["Down"] = True
            elif controlMatrix[self.posX][self.posY] == 23:
                self.moves["Left"] = True
                self.moves["Up"] = True
                self.moves["Down"] = True
            elif controlMatrix[self.posX][self.posY] == 24:
                self.moves["Up"] = True
                self.moves["Down"] = True
                self.moves["Right"] = True
    
    def update(self):
        if self.availableMoves(self.direction):
            if self.direction == 0: #Arriba
                self.posY -= self.speed
            elif self.direction == 1: #Derecha
                self.posX += self.speed
            elif self.direction == 2: #Abajo
                self.posY += self.speed
            elif self.direction == 3: #Izquierda
                self.posX += self.speed
              
                
    # Arriba = 0, Derecha = 1, Abajo = 2, Izquierda = 3
    def draw(self, direction):
        rotation_angle = 0  
        if direction == 0:  
            rotation_angle = 270
        elif direction == 1:  
            rotation_angle = 0
        elif direction == 2:  
            rotation_angle = 90
        elif direction == 3:  
            rotation_angle = 180
        #pygame.transform.rotate(self.sprite, rotation_angle)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.sprite)  # Use the texture ID from load_texture
        glPushMatrix()
        glTranslatef(self.initialPosition[0], self.initialPosition[1], self.initialPosition[2])
        glRotatef(rotation_angle, 0, 0, 1)  # Rota en torno al eje Z
        glScaled(1, 1, 1) # Cambio de escala en caso de ser necesatio
        glBegin(GL_QUADS)
        # Adjusted to draw the texture in the xz plane with y fixed for height.
        size = 8  # The size of the Pac-Man texture in the world space
        x = 0  # Fixed y coordinate since Pac-Man is on the ground
        glTexCoord2f(0, 0); glVertex3f(x, 0, 0)
        glTexCoord2f(1, 0); glVertex3f(x, size, 0)
        glTexCoord2f(1, 1); glVertex3f(x, size, size)
        glTexCoord2f(0, 1); glVertex3f(x, 0, size)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

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