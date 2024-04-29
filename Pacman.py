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
Zpx=np.array([0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,16])

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
        self.posZ=0
        #Se inicializa una posicion 0,0 en el tablero
        self.Position = [162, 1, 161]
        #Velocidad en los 3 ejes
        self.Direction=[1,0,1]
        #Se declara la dirección de giro
        self.direction = 0
        #Se declaran los movimientos posibles
        self.moves = {
            "Up": False,
            "Right": True,
            "Left": False,
            "Down": True
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
        if controlMatrix[self.posX][self.posZ] == 0:
            if Xpx[self.posX] == -1:
                self.moves["Right"] = True
                self.moves["Left"] = True
            elif Zpx[self.posZ] == -1:
                self.moves["Up"] = True
                self.moves["Down"] = True
        if controlMatrix[self.posX][self.posZ] > 0:
            if controlMatrix[self.posX][self.posZ] == 11:
                self.moves["Left"] = False
                self.moves["Right"] = False
                self.moves["Up"] = True
                self.moves["Down"] = False
            elif controlMatrix[self.posX][self.posZ] == 12:
                self.moves["Left"] = False
                self.moves["Right"] = False
                self.moves["Up"] = False
                self.moves["Down"] = True
            elif controlMatrix[self.posX][self.posZ] == 13:
                self.moves["Left"] = True
                self.moves["Right"] = False
                self.moves["Up"] = False
                self.moves["Down"] = False
            elif controlMatrix[self.posX][self.posZ] == 17:
                self.moves["Left"] = True
                self.moves["Right"] = False
                self.moves["Up"] = True
                self.moves["Down"] = False
            elif controlMatrix[self.posX][self.posZ] == 19:
                self.moves["Up"] = True
                self.moves["Right"] = True
                self.moves["Up"] = False
                self.moves["Down"] = False
            elif controlMatrix[self.posX][self.posZ] == 21:
                self.moves["Left"] = True
                self.moves["Right"] = True
                self.moves["Up"] = True
                self.moves["Down"] = False
            elif controlMatrix[self.posX][self.posZ] == 22:
                self.moves["Left"] = True
                self.moves["Right"] = True
                self.moves["Up"] = False
                self.moves["Down"] = True
            elif controlMatrix[self.posX][self.posZ] == 23:
                self.moves["Up"] = True
                self.moves["Down"] = True
                self.moves["Right"] = False
                self.moves["Left"] = True
            elif controlMatrix[self.posX][self.posZ] == 24:
                self.moves["Up"] = True
                self.moves["Down"] = True
                self.moves["Right"] = True
                self.moves["Left"] = False
    
    def update(self):
        self.availableMoves()  # Ver movimientos disponibles
        
        new_x = self.Position[0] + self.Direction[0]
        new_z = self.Position[2] + self.Direction[2]

        if 0 <= new_x < len(Xpx)-1 and 0 <= new_z < len(Zpx)-1:  # Rango válido
            if self.direction == 0 and self.moves["Up"]:  # Arriba
                self.posZ -= self.speed
            elif self.direction == 1 and self.moves["Right"]:  # Derecha
                self.posX += self.speed
            elif self.direction == 2 and self.moves["Down"]:  # Abajo
                self.posZ += self.speed
            elif self.direction == 3 and self.moves["Left"]:  # Izquierda
                self.posX -= self.speed
            self.Position[0] = self.posX + 166 # 166 es el "Offset"
            self.Position[2] = self.posZ  + 167 # 167 es el "Offset"
        else:
            print("PacMan out of bounds : new_x={new_x}, new_z={new_z}")

              
                
    # Arriba = 0, Derecha = 1, Abajo = 2, Izquierda = 3
    def draw(self, direction):  
        #pygame.transform.rotate(self.sprite, rotation_angle)
        rotation_angle = 0
        if direction == 0:  
            rotation_angle = 90 #Derecha
        elif direction == 1:  
            rotation_angle = 90 #Abajo
        elif direction == 2: 
            rotation_angle = 270 #Izquierda
        elif direction == 3:  
            rotation_angle =  270 #Arriba
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.sprite)  
        glPushMatrix()
        glTranslatef(*self.Position)
        if direction == 0 or direction == 2:
            glRotatef(rotation_angle, 0, 0, 1)  # Rota en torno al eje Z
        elif direction == 1 or direction == 3:
            glRotatef(rotation_angle, 0,1,0)
        glScaled(1, 1, 1) # Cambio de escala en caso de ser necesatio
        size = 6 
        glBegin(GL_QUADS)
        x = 0  
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
