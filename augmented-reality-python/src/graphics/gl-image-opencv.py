# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
import pygame
import OpenGL
import cv2
import Image
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from threaded_webcam import WebCamVideoStream

# set webcam video stream
webcam = WebCamVideoStream().start()


# ------------------------
#   Wall FUNCTION
# ------------------------
def wall(image):
    # set the OpenGL wall parameters
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


# ------------------------
#   Main Loop FUNCTION
# ------------------------
def GlMainLoop(img):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # convert image to OpenGL texture format
        tx_image = webcam.read()
        tx_image = Image.fromarray(tx_image)
        ix = tx_image.size[0]
        iy = tx_image.size[1]
        tx_image = tx_image.tobytes('raw', 'BGRX', 0, -1)
        # create texture
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, tx_image)
        glLoadIdentity()
        glTranslatef(0, 0, -5)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # call OpenGL wall function
        wall(img)
        # start pygame and display
        pygame.display.flip()
        pygame.time.wait(50)


# ------------------------
#   MAIN FUNCTION
# ------------------------
def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF|OPENGL)
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
    # call GlMainLoop function
    GlMainLoop(img)


main()
