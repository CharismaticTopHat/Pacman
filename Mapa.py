import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

# Se carga el archivo de la clase Cubo
import sys
sys.path.append('..')
from Ghost import Ghost
from Pacman import Pacman

screen_width = 500
screen_height = 500
#vc para el obser.
FOVY=39.0
ZNEAR=1.0
ZFAR=1000.0
#Variables para definir la posicion del observador
#gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X = 92.0
EYE_Y = 250.0
EYE_Z = 92.0
CENTER_X = 90.0
CENTER_Y = 0.0
CENTER_Z = 90.0
UP_X=0
UP_Y=0
UP_Z=1
#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500
Z_MIN=-500
Z_MAX=500
#Dimension del plano
DimBoard = 180

#Variables para el control del observador
theta = 0.0
radius = 300

#Carga del CSV
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_PATH, 'mapa pacman.csv')

#Arreglo para el manejo de texturas
textures = []
filename1 = "PacMan_map.bmp"
filename2 = "PacMan.bmp"
filename3 = "PacMan_Ghost2.bmp"
filename4 = "PacMan_Ghost3.bmp"
filename5 = "PacMan_Ghost4.bmp"
filename6 = "PacMan_Ghost1.bmp"
pygame.init()

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN,0.0,0.0)
    glVertex3f(X_MAX,0.0,0.0)
    glEnd()
    #Y axis in green
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,Y_MIN,0.0)
    glVertex3f(0.0,Y_MAX,0.0)
    glEnd()
    #Z axis in blue
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0,0.0,Z_MIN)
    glVertex3f(0.0,0.0,Z_MAX)
    glEnd()
    glLineWidth(1.0)

def Texturas(filepath):
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image, "RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)

def Init():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Pac-Man")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    Texturas(filename1)

    global pacman
    pacman = Pacman([85, 1, 47], 264, 396, filename2)
    global ghosts, randomGhost1, randomGhost2, randomGhost3
    ghosts = []
    randomGhost1 = Ghost([161, 1, 162], 0, 0, filename3)
    randomGhost2 = Ghost([161, 1, 9], 0, 400, filename4)
    randomGhost3 = Ghost([10, 1, 9], 400, 400, filename5)
    ghosts.append(randomGhost1)
    ghosts.append(randomGhost2)
    ghosts.append(randomGhost3)


#Se mueve al observador circularmente al rededor del plano XZ a una altura fija (EYE_Y)
def lookat():
    global EYE_X
    global EYE_Z
    global radius
    EYE_X = radius * (math.cos(math.radians(theta)) + math.sin(math.radians(theta)))
    EYE_Z = radius * (-math.sin(math.radians(theta)) + math.cos(math.radians(theta)))
    glLoadIdentity()
    gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
    #glutPostRedisplay()
    
def Plano():
    #Se dibuja el plano gris
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()   
    
def PlanoTexturizado():
    #Activate textures
    glColor3f(1.0,1.0,1.0)
    glEnable(GL_TEXTURE_2D)
    #front face
    glBindTexture(GL_TEXTURE_2D, textures[0])    
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(0, 0, 0)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(DimBoard, 0, 0)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(DimBoard, 0, DimBoard)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(0, 0, DimBoard)
    glEnd()              
    glDisable(GL_TEXTURE_2D)


def display(direction):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Axis()
    # Plano()
    PlanoTexturizado()
    # pc.draw()
    pacman.draw()
    pacman.update(direction)
    for ghost in ghosts:
        ghost.draw()
        ghost.update()

done = False
Init()
direction = [0, 0, 0]  # Inicializamos direction
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Modificar la dirección según la tecla presionada
            if event.key == pygame.K_UP:
                direction = [0, 0, 1]  # Mover hacia arriba en el eje Z
            elif event.key == pygame.K_DOWN:
                direction = [0, 0, -1]  # Mover hacia abajo en el eje Z
            elif event.key == pygame.K_LEFT:
                direction = [1, 0, 0]  # Mover hacia la izquierda en el eje X
            elif event.key == pygame.K_RIGHT:
                direction = [-1, 0, 0]  # Mover hacia la derecha en el eje X

    display(direction)

    pygame.display.flip()
    pygame.time.wait(20)

pygame.quit()
