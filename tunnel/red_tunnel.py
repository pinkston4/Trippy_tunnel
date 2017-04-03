from .tunnel import Tunnel


class RedTunnel(Tunnel):
    """

    """

    def __init__(self):
        Tunnel.__init__(self)
        # the vertices of the cube
        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )
        self.colors = (
            (0, 0, 0),
            (1, 0, 0),
            (0, 0, 0),
            (1, 0, 0),
            (1, 0, 0),
            (1, 0, 0),
            (0, 0, 0),
            (1, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (1, 0, 0),
            (1, 0, 0),
        )
