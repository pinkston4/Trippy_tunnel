from .tunnel import Tunnel


class BlueTunnel(Tunnel):
    """

    """

    def __init__(self):
        Tunnel.__init__(self)
        # the vertices of the cube
        self.vertices = (
            (1, -1, -13),
            (1, 1, -13),
            (-1, 1, -13),
            (-1, -1, -13),
            (1, -1, -11),
            (1, 1, -11),
            (-1, -1, -11),
            (-1, 1, -11)
        )
        self.colors = (
            (0, 0, 0),
            (0, 0, 1),
            (0, 0, 0),
            (0, 0, 1),
            (0, 0, 1),
            (0, 0, 1),
            (0, 0, 0),
            (0, 0, 1),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 1),
            (0, 0, 1),
        )
