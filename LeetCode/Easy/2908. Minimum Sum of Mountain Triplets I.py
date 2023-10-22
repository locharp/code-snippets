class Solution:

    def minimumSum( self, nums: List[int] ) -> int:
        n = len( nums ) - 1
        ans = x = inf

        for i in range( len( nums ) - 2 ):
            if nums[i] < x:
                x = nums[i]

                for j in range( i + 1, n ):
                    if nums[j] > nums[i]:
                        y = nums[j]
                        
                        for k in range( j + 1, len( nums ) ):
                            if nums[k] < nums[j]:
                                ans = min( ans, nums[i] + nums[j] + nums[k] )
        
        return ans if ans != inf else -1



from sortedcontainers import SortedSet

class Solution2:

    def minimumSum( self, nums: List[int] ) -> int:

        a = SortedSet( { ( 51, ) } )
        m = inf

        for num in nums:
            i = t = 0

            while i < len( a ):
                if len( a[i] ) > 2:
                    if num < a[i][2] and num < a[i][1] and sum( a[i][ : 2 ] ) + num < m:
                        w = ( a[i][0], a[i][1], num )
                        a.pop( i )
                        a.add( w )
                        m = sum( a[i] )

                        t = i + 1
                elif len( a[i] ) > 1:
                    if num < a[i][1]:
                        if sum( a[i] ) + num < m:
                            a.add( ( a[i][0], a[i][1], num ) )
                            m = sum( a[ i + 1 ] )
                            t = i + 2
                    elif num > a[i][1]:
                        if len( a[-1] ) < 3 or a[i][0] + num + 1 < m:
                            a.add( ( a[i][0], num ) )
                else:
                    if num > a[i][0] and a[i][0] + num + 1 < m:
                        while i + 1 < len( a ) and len( a[ i + 1 ] ) < 2:
                            a.pop( i + 1 )

                        a.add( ( a[i][0], num ) )
                        i += 1

                i += 1
            
            if t > 0:
                a = SortedSet( a[ : t ] )

            if num < a[0][0]:
                a.add( ( num, ) )
            
        return m if m != inf else -1
