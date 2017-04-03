from .tunnel import Tunnel


class MainTunnel(Tunnel):
    """

    """

    def __init__(self):
        Tunnel.__init__(self)
        # the vertices of the cube
        self.vertices = (
            (2, -2, -19),
            (2, 2, -19),
            (-2, 2, -19),
            (-2, -2, -19),
            (2, -2, 3),
            (2, 2, 3),
            (-2, -2, 3),
            (-2, 2, 3)
        )
        self.colors = None
