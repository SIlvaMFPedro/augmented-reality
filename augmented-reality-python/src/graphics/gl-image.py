# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# ------------------------
#   MAIN FUNCTION
# ------------------------
def main():
    pygame.init()
    pygame.display.set_mode((600,600), DOUBLEBUF|OPENGL)


main()

# Load the pygame parameters
img = pygame.image.load('/home/pedro/Documents/augmented-reality/augmented-reality-python/assets/stones.jpg')
textureData = pygame.image.tostring(img, "RGB", 1)
width = img.get_width()
height = img.get_height()

# Load OpenGL parameters
im = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, im)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
glEnable(GL_TEXTURE_2D)


# ------------------------
#   WALL FUNCTION
# ------------------------
def wall():
    # set OpenGL parameters for the wall
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-4, -4, -16)
    glTexCoord2f(0, 1)
    glVertex3f(-4, 4, -16)
    glTexCoord2f(1, 1)
    glVertex3f(4, 4, -8)
    glTexCoord2f(1, 0)
    glVertex3f(4, -4, -8)
    glEnd()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    glLoadIdentity()
    gluPerspective(45, 1, 0.05, 100)
    glTranslatef(0, 0, -5)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # set OpenGL wall parameters
    wall()
    # start pygame
    pygame.display.flip()
    pygame.time.wait(50)