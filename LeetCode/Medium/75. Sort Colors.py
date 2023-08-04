class Solution:
    def sortColors( self, nums: List[int] ) -> None:
        counts = [ 0 ] * 3
        
        for num in nums:
            counts[num] += 1
        
        nums[ : ] = [ 0 ] * counts[0] + [ 1 ] * counts[1] + [ 2 ] * counts[2]