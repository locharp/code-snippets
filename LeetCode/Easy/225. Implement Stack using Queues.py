class MyStack:

    def __init__( self ):
        self.queue = []
        self.size = 0
        
    def push( self, x: int ) -> None:
        self.queue.append( x )
        self.size += 1
        
        for _ in range( self.size - 1 ):
            self.queue.append( self.queue.pop( 0 ) )

    def pop( self ) -> int:
        self.size -= 1
        
        return self.queue.pop( 0 )
        
    def top( self ) -> int:
        tmp = self.pop()
        self.push( tmp )
        
        return tmp

    def empty( self ) -> bool:
        return self.size == 0