class InfiniteArray:
    def __init__( self ):
        self.a = [ False ] * 10000

    def setAllTrue( self ) -> None:
        self.a = [ True ] * 10000

    def setAllFalse( self ) -> None:
        self.a = [ False ] * 10000

    def setIndexTrue( self, index: int ) -> None:
        self.a[index] = True

    def setIndexFalse( self, index: int ) -> None:
        self.a[index] = False

    def getIndex( self, index: int ) -> bool:
        return self.a[index]
