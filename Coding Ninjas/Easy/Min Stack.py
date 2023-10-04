from heapq import heappop, heappush

class minStack:
    def __init__( self ):
        self.Stack = []
        self.Min = []
        self.index = 0
        self.d = {}


    
    def push( self, num: int ) -> None:
        self.index += 1
        self.d[self.index] = num 
        heappush( self.Min, ( num, self.index ) )
        self.Stack.append( self.index )


    
    def pop( self ) -> int:
        while len( self.Stack ) > 0:
            i = self.Stack.pop()
            
            if i in self.d:
                return self.d.pop( i )
            
        return -1
    
    
    
    def top( self ) -> int:
        while len( self.Stack ) > 0:
            if self.Stack[-1] in self.d:
                return self.d[ self.Stack[-1] ]
            else:
                self.Stack.pop()
                
        return -1
    

    
    def getMin( self ) -> int:
        while len( self.Min ) > 0:
            i, j = self.Min[0]
            
            if j in self.d:
                return i
            else:
                heappop( self.Min )
                
        return -1
