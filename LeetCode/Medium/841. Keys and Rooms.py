class Solution:
    
    def canVisitAllRooms( self, rooms: List[ List[int] ] ) -> bool:
        
        s = { 0 }
        t = { i for i in range( len( rooms ) ) }
        
        while len( s ) > 0 and len( t ) > 0:
            o = s.pop()
            
            if o in t:
                t.remove( o )
                
                for i in rooms[o]:
                    s.add( i )
                    
        return len( t ) < 1
