class Solution:
    def canFinish( self, numCourses: int, prerequisites: List[List[int]] ) -> bool:
        o = [ [] for i in range( numCourses ) ]
        m = [ [] for i in range( numCourses ) ]
        q = deque()
        s = set()
        
        for u, v in prerequisites:
            o[u].append( v )
            m[v].append( u )
            
        for i in range( numCourses ):
            if len ( o[i] ) == 0:
                q.append( i )
                s.add( i )
                
        while len( q ) > 0:
            p = q.pop()
            
            for r in m[p]:
                o[r].remove( p )
                
                if len( o[r] ) == 0:
                    q.append( r )
                    s.add( r )
                    
        return len( s ) == numCourses