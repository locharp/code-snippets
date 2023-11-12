class NQueue:
    
    def __init__( self, n, s ):
        
        self.q = [ [] for i in range( n + 1 ) ]
        self.m = s
        self.n = 0
        
        
        
    def enqueue( self, x, m ):
        
        if self.n < self.m:
            self.q[m].append( x )
            self.n += 1
            
            return True
        else:
            return False
        
        
        
    def dequeue( self, m ):
        
        if len( self.q[m] ) > 0:
            self.n -= 1
            
            return self.q[m].pop( 0 )
        else:
            return -1
