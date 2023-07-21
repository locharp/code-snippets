class Solution:
    def findNumberOfLIS( self, nums: List[int] ) -> int:
        n = len( nums )
        p = [ 1 ] * n
        c = [ 1 ] * n
        
        for i in range( n ):
            for j in range( i ):
                if nums[i] > nums[j]:
                    o = p[j] + 1
                    
                    if p[i] < o:
                            p[i] = o
                            c[i] = c[j]
                    elif p[i] == o:
                            c[i] += c[j]
                            
        return sum( c[i] for i in range( n ) if p[i] == max( p ) )