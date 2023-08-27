class Solution:
    def canCross( self, stones: List[int] ) -> bool:
        q, v = deque(), set()
        q.append( ( 0, 0 ) )
        n = len( stones )
        m = n - 1
        
        while len( q ) > 0:
            j, k = q.pop()
            
            for i in range( j + 1, n ):
                d = stones[i] - stones[j]
                
                if ( i, d ) in v:
                    continue
                elif d > k - 2 and d < k + 2:
                    if i == m:
                        return True
                    
                    v.add( ( i, d ) )
                    q.append( ( i, d ) )
                    
                    if d - k > 0:
                        break
                else:
                    if d - k > 0:
                        break
                        
        return False