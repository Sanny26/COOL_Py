from base import IO, Object

class Cons(Object):

    xcar = None
    xcdr = None
    
    def isNil(self, ) -> bool:
            return False    
    
    def init(self, hd : int,tl : str,) -> Object:
            self.xcar = hd
            self.xcdr = tl
            return self
    
    xx = 10

