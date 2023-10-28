class Solution:
    
    def canVisitAllRooms( self, rooms: List[ List[int] ] ) -> bool:
        
        s = { 0 }
        t = { i for i in range( 1, len( rooms ) ) }
        
        while len( s ) > 0 and len( t ) > 0:
            o = s.pop()
            
            for i in rooms[o]:
                if i in t:
                    s.add( i )
                    t.remove( i )
            
        return len( t ) < 1
