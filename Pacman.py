import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np

#Arreglo para el manejo de texturas
textures = []
filename1 = "Pac-Man.bmp"

controlMatrix = [20,0,22,0,0,0,22,13,0,14,22,0,0,0,22,0,18,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 11,0,24,0,18,0,19,0,22,0,17,0,20,0,23,0,11,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 12,0,0,0,0,0,20,0,21,0,18,0,0,0,0,0,12,
                 24,0,23,0,0,0,0,0,0,0,0,0,0,0,24,0,23,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,11,0,24,0,17,0,0,0,19,0,23,0,11,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,12,0,24,0,18,0,0,0,20,0,23,0,12,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 24,0,23,0,0,0,0,0,0,0,0,0,0,0,24,0,23,
                 11,0,0,0,0,0,19,0,22,0,17,0,0,0,0,0,11,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 12,0,24,0,17,0,20,0,21,0,18,0,19,0,23,0,12,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 19,0,21,0,0,0,21,13,0,14,21,0,0,0,21,0,17]

class Pacman:
    
    def __init__(self, dim, vel): #position,direction,map (csv)
        
        self.DimBoard = dim
        #Se inicializa una posicion 0,0 en el tablero
        self.Position = [50,1,42]
        #Se inicializa un vector de direccion aleatorio
        self.Direction = [0,0,0]
        #Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0]*self.Direction[0] + self.Direction[2]*self.Direction[2])
        self.Direction=(self.Direction/m)
        #Se cambia la maginitud del vector direccion
        self.Direction[0] *= vel
        self.Direction[2] *= vel


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                
            elif event.type == pygame.K_UP:     
            elif event.type == pygame.K_LEFT:
            elif event.type == pygame.K_RIGHT:
                if event.key == pygame.K_RIGHT:
                    if theta > 359.0:
                        theta = 0
                    else:
                        theta += 1.0
                    lookat()
                if event.key == pygame.K_LEFT:
                    if theta < 1.0:
                        theta = 360.0
                    else:
                        theta += -1.0
                    lookat()
                if event.key == pygame.K_ESCAPE:
                    done = True

        display()

    pygame.display.flip()
    pygame.time.wait(5)
    
    def update(self):
            new_x = self.Position[0] + self.Direction[0]
            new_z = self.Position[2] + self.Direction[2]
        
        #detecc de que el objeto no se salga del area de navegacion
            if (abs(new_x) < self.DimBoard):
                self.Position[0] = new_x
            else:
                self.Direction[0] *= -1.0
                self.Position[0] += self.Direction[0]
                
            if(abs(new_z) < self.DimBoard):
                self.Position[2] = new_z
            else:
                self.Direction[2] *= -1.0
                self.Position[2] += self.Direction[2]

    def Texturas(filepath):
        textures.append(glGenTextures(1))
        id = len(textures) - 1
        glBindTexture(GL_TEXTURE_2D, textures[id])
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        image = pygame.image.load(filepath).convert()
        w, h = image.get_rect().size
        image_data = pygame.image.tostring(image,"RGBA")
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        glGenerateMipmap(GL_TEXTURE_2D) 
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(5,5,5)
        glColor3f(1.0, 1.0, 1.0)
        self.drawFaces()
        glPopMatrix()