import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np

#Arreglos para posición en pixeles
PCposX=np.array([20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,18])
PCposZ=np.array([20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,19])

direction = 0

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
    def __init__(self, dim, vel, sprite_filepath): 
        #Se initicializa una variable con el tamaño del mapa
        self.DimBoard = dim
        #Se inicializa una posicion 0,0 en el tablero
        self.Position = [25,1,25]
        #Se inicializa un vector de direccion en torno al eje X
        self.Direction = [1,0,0]
        #Se normaliza el vector de direccion
        m = math.sqrt(self.Direction[0]*self.Direction[0] + self.Direction[2]*self.Direction[2])
        self.Direction=(self.Direction/m)
        #Se cambia la maginitud del vector direccion
        self.Direction[0] *= vel
        self.Direction[2] *= vel
        #Se carga el Sprite de PacMan
        self.sprite= pygame.image.load(sprite_filepath)

    # Arriba = 0, Derecha = 1, Abajo = 2, Izquierda = 3
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP: 
                    direction = 0 
                elif event.type == pygame.K_RIGHT:
                    direction = 1
                elif event.type == pygame.K_DOWN:
                    direction = 2
                elif event.type == pygame.K_LEFT:
                    direction = 3
    
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
    
    def draw(self, sprite, direction):
        rotation_angle = 0  
        if direction == 0:  
            rotation_angle = 270
        elif direction == 1:  
            rotation_angle = 0
        elif direction == 2:  
            rotation_angle = 90
        elif direction == 3:  
            rotation_angle = 180
        rotated_sprite = pygame.transform.rotate(sprite, rotation_angle)
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(1, 1, 1)
        glBindTexture()
        # Example: glBindTexture(GL_TEXTURE_2D, textures[0])

        # Apply rotation to OpenGL object
        glRotatef(rotation_angle, 0, 1, 0)  # Example rotation around the Y-axis
        
        # Your OpenGL drawing code here
        # For example: glBegin(GL_TRIANGLES) ... glEnd()

        glPopMatrix()
