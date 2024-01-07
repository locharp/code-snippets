class Stack:
    
    def __init__( self ):
        
        self.stack = []
        
        
        
    def push( self, x ):
        
        self.stack.append( x )
        
        return True
        
        
        
    def pop(self):
        
        if len( self.stack ) < 1:
            return -1
        else:
            return self.stack.pop()
            
            
            
    def top( self ):
        
        if len( self.stack ) < 1:
            return -1
        else:
            return self.stack[-1]
            
            
            
    def isEmpty( self ):
    
        return len( self.stack ) < 1
        
        
        
    def size(self):
        
        return len( self.stack )
