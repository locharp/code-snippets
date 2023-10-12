class Solution:
    def findInMountainArray( self, target: int, mountain_arr: 'MountainArray' ) -> int:
        j = o = mountain_arr.length() - 1
        i, k = 0, 1
        d = {}
        
        while k < j:
            m = ( k + j ) // 2
            n = m + 1
            
            if m not in d:
                d[m] = mountain_arr.get( m )
            
            if n not in d:
                d[n] = mountain_arr.get( n )
                
            if d[m] < d[n]:
                k = n
            else:
                j = m
                
        while i <= j:
            m = ( i + j ) // 2
            
            if m not in d:
                d[m] = mountain_arr.get( m )
                
            if d[m] > target:
                j = m - 1
            elif d[m] < target:
                i = m + 1
            else:
                return m
            
        while k <= o:
            m = ( k + o ) // 2
            
            if m not in d:
                d[m] = mountain_arr.get( m )
                
            if d[m] < target:
                o = m - 1
            elif d[m] > target:
                k = m + 1
            else:
                return m
            
        return -1
