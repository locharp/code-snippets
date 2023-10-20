class NestedIterator:
    
    def __init__( self, nestedList: [NestedInteger] ):
        
        self.a = nestedList
        self.i = 0
        self.list = None
        
        
        
    def next( self ) -> int:
        if self.a[self.i].isInteger():
            self.i += 1
            
            return self.a[ self.i - 1 ].getInteger()
        
        return self.list.next()
            
            
            
    def hasNext( self ) -> bool:
        
        if self.list is not None:
            if self.list.hasNext():
                return True
            
            self.list = None
            self.i += 1
                
        if len( self.a ) > self.i:
            if self.a[self.i].isInteger():
                return True
            
            self.list = NestedIterator( self.a[self.i].getList() )
            
            return self.hasNext()
            
        return False
