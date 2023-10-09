class MyCircularQueue:

    def __init__( self, k: int ):
        
        self.queue = [ -1 ] * k
        self.head = self.tail = 0
        self.size = k
        
        
        
    def enQueue( self, value: int ) -> bool:
        
        if not self.isFull():
            self.queue[self.tail] = value
            self.tail = ( self.tail + 1 ) % self.size
            
            return True
        
        
        
    def deQueue( self ) -> bool:
        
        if not self.isEmpty():
            self.queue[self.head] = -1
            self.head = ( self.head + 1 ) % self.size
            
            return True
        
        
        
    def Front( self ) -> int:
        
        return self.queue[self.head]
        
        
        
    def Rear( self ) -> int:
        
        return self.queue[ ( self.tail - 1 + self.size ) % self.size ]
        
        
        
    def isEmpty( self ) -> bool:
        
        return self.queue[self.head] == -1
    
    
    
    def isFull( self ) -> bool:
        
        return self.queue[self.tail] != -1
