from sortedcontainers import SortedList

class Solution:

    def constrainedSubsetSum( self, nums: List[int], k: int ) -> int:
        
        a = SortedList()

        for i in range( k ):
            if len( a ) > 0:
                nums[i] += a[-1]

            if nums[i] > 0:
                a.add( nums[i] )
                
                while a[0] < nums[i]:
                    a.pop( 0 )

        for i in range( k, len( nums ) ):
            if len( a ) > 0:
                nums[i] += a[-1]

                if a[-1] == nums[ i - k ]:
                    a.pop()

            if nums[i] > 0:
                a.add( nums[i] )
                
                while a[0] < nums[i]:
                    a.pop( 0 )

        return max( nums )
