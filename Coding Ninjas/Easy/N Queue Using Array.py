class NQueue:
    
    def __init__( self, n, s ):
        
        self.q = [ [] for i in range( n + 1 ) ]
        self.s = s
        
        
        
    def enqueue( self, x, m ):
        
        if len( self.q[m] ) < self.s:
            self.q[m].append( x )
            
            return True
        else:
            return False
            
            
            
    def dequeue( self, m ):
        
        if len( self.q[m] ) > 0:
            return self.q[m].pop( 0 )
        else:
            return -1
