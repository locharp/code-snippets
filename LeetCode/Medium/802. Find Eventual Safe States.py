class Solution:
    def eventualSafeNodes( self, graph: List[List[int]] ) -> List[int]:
        q = deque()
        d = defaultdict( list )
        ans = []
        
        for i in range( len( graph ) ):
            if len( graph[i] ) == 0:
                q.append( i )
            
            for j in graph[i]:
                d[j].append( i )
                
        while len( q ) > 0:
            i = q.pop()
            ans.append( i )
            
            for j in d.get( i, [] ):
                graph[j].remove( i )
                
                if len( graph[j] ) == 0:
                    q.append( j )
                    
        return sorted( ans )