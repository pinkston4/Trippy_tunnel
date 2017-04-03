from OpenGL.GL import *


class Tunnel:
    """
    The base Tunnel class that draws the cubes that creates the illusion of a tunnel
    methods:
        __init__
        draw_cube
    """
    def __init__(self):
        # self.edges is a tuple of tuples containing indexes of vertices
        self.edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )
        # the six surfaces of a cube, used for coloring them
        self.surfaces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6)
        )


    def draw_cube(self):
        """
        draws and colors the cubes
        """
        if self.colors != None:
            glBegin(GL_QUADS)
            for surface in self.surfaces:
                x = 0
                for vertex in surface:
                    glColor3fv(self.colors[x])
                    glVertex3fv(self.vertices[vertex])
                    x += 1

            glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
