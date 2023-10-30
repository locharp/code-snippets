class CircularQueue:

    def __init__( self, n ):
        
        self.maxsize = n
        self.q = []



    def enqueue( self, value ):
        
        if self.maxsize == len( self.q ):
            return False
            
        self.q.append( value )

        return True



    def dequeue( self ):
        
        if len( self.q ) < 1:
            return -1
        
        return self.q.pop( 0 )
