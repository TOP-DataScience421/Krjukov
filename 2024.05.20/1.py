

class Tetrahedron:
    
    def __init__(self, edge: float ) -> None:
        self.edge = edge

    def surface(self) -> float:
        s = (self.edge**2)*(3**0.5)
        return s
    
    def volume(self) -> float:
        v = ((self.edge**3)/12)*(2**0.5)
        return v


"""
>>> t1 = Tetrahedron(5)
>>> t1.edge
5
>>> t1.surface()
43.30127018922193
>>> t1.volume()
14.73139127471974
>>> t1.edge = 6
>>> t1.surface()
62.35382907247958
>>> 
"""