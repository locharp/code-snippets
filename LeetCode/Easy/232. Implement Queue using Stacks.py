class MyQueue:

    def __init__( self ):
        
        self.a = []
        
        

    def push( self, x: int ) -> None:
        
        self.a.append( x )
        
        

    def pop( self ) -> int:
        
        return self.a.pop( 0 )
    
    

    def peek( self ) -> int:
        
        return self.a[0]
    
    

    def empty( self ) -> bool:
        
        return len ( self.a ) == 0
