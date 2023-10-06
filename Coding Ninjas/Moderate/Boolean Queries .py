from collections import *

class InfiniteArray:
    def __init__( self ):
        self.d = defaultdict( self.f )

    def setAllTrue( self ) -> None:
        self.d = defaultdict( self.t )

    def setAllFalse( self ) -> None:
        self.d = defaultdict( self.f )

    def setIndexTrue( self, index: int ) -> None:
        self.d[index] = True

    def setIndexFalse( self, index: int ) -> None:
        self.d[index] = False

    def getIndex( self, index: int ) -> bool:
        return self.d[index]
    
    def f( self ) -> bool:
        return False
    
    def t( self ) -> bool:
        return True
