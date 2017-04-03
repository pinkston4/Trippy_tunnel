import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from tunnel.red_tunnel import RedTunnel
from tunnel.green_tunnel import GreenTunnel
from tunnel.blue_tunnel import BlueTunnel
from tunnel.big_tunnel import MainTunnel


class TrippyTunnel(object):
    """
    The Trippy class is the main class of the application
    methods:
        __init__
        looper
    """
    def __init__(self, screen_width, screen_height):
        """
        Initializes application, sets the screen size, initializes cubes,
        sets the perspective, and calls the loop
        :param screen_width: width of screen
        :param screen_height: height of screen
        """
        self.display = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        self.percpective = gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        self.step_back = glTranslatef(0.0, 0.0, -15)
        self.red_tunnel = RedTunnel()
        self.green_tunnel = GreenTunnel()
        self.blue_tunnel = BlueTunnel()
        self.main_tunnel = MainTunnel()
        self.tunnels = (self.main_tunnel, self.blue_tunnel, self.green_tunnel, self.red_tunnel)
        self.tunnel_chain = self.build_tunnel_chain()
        self.looper()

    def build_tunnel_chain(self):
        """

        :return:
        """
        pass

    def looper(self):
        """
        the while loop that makes the app run, listens for the quit event
        rotates and re-draws cubes/tunnels
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glRotatef(1, 0, 0, -10)
            glTranslatef(0, 0, 0.1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.main_tunnel.draw_cube()
            self.blue_tunnel.draw_cube()
            self.green_tunnel.draw_cube()
            self.red_tunnel.draw_cube()
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == '__main__':
    width, height = 1280, 720
    pygame.init()
    window = TrippyTunnel(width, height)
