class Solution:
    
    def findChampion( self, grid: List[ List[int] ] ) -> int:
        
        n = len( grid )
        a = [ 0 ] * n
        
        for i in grid:
            for j in range( n ):
                a[j] += i[j]
                
        ans = -1
        
        for i in range( n ):
            if a[i] == 0:
                if ans == -1:
                    ans = i
                else:
                    ans == -1
                    break
                    
        return ans
