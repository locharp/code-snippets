class Solution:
    
    def isPathCrossing( self, path: str ) -> bool:
        
        p = q = 0
        s = { ( p, q ) }
        
        for i in path:
            if i == "N":
                p += 1
            elif i == "S":
                p -= 1
            elif i == "E":
                q += 1
            else:
                q -= 1
                
            r = ( p, q )
            
            if r in s:
                return True
            else:
                s.add( r )
                
        return False
