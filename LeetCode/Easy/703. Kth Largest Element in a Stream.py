class KthLargest:

    def __init__( self, k: int, nums: List[int] ):
        self.a = sorted( nums )
        self.a.append( 10001 )
        self.size = len( self.a )
        self.k = k + 1
        
    def add( self, val: int ) -> int:
        self.size += 1
        
        for i in range( self.size ):
            if self.a[i] >= val:
                self.a.insert( i, val )
                break

        return self.a[-self.k]