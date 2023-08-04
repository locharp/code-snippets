class Solution:
    def sortArray( self, nums: List[int] ) -> List[int]:
        def sort( arr, d ):
            buckets = [ [] for _ in range( 10 ) ]
            
            for num in arr:
                buckets[ num // d % 10 ].append( num )
                
            i = 0
            for bucket in buckets:
                for num in bucket:
                    arr[i] = num
                    i += 1
            
        m, n = 0, 0
        p, q = [], []
        
        for num in nums:
            if num < 0:
                x = -num
                q.append( x )
                
                if n < x:
                    n = x
            else:
                p.append( num )
                
                if m < num:
                    m = num
                
        o = 1
        while m > 0:
            sort( p, o )
            o *= 10
            m //= 10
            
        o = 1
        while n > 0:
            sort( q, o )
            o *= 10
            n //= 10
            
        return [ -i for i in q[ : : -1 ] ] + p