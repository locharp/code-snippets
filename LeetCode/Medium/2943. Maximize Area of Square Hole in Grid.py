class Solution:
    
    def f( self, a ):
        
        a.sort()
        c = j = 1
        i = 0
        
        while j < len( a ):
            if a[j] - 1 != a[ j - 1 ]:
                c = max( c, j - i )
                i = j
                
            j += 1
            
        return max( c, j - i )
    
            
        
    def maximizeSquareHoleArea( self, n: int, m: int, hBars: List[int], vBars: List[int] ) -> int:
        
        return ( min( self.f( hBars ), self.f( vBars ) ) + 1 ) ** 2
