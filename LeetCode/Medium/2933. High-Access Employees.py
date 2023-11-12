class Solution:
    
    def findHighAccessEmployees( self, access_times: List[ List[str] ] ) -> List[str]:
        
        d = defaultdict( list )
        ans = []
        
        for i, j in access_times:
            d[i].append( int( j ) )
        
        for p, q in d.items():
            if len( q ) < 3:
                continue
                
            q.sort()
            i = 0
            
            for j in q[ 2 : ]:
                if j - q[i] < 100:
                    ans.append( p )
                    break
                    
                i += 1
                
        return ans
