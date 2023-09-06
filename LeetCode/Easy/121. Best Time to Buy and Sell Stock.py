class Solution:
    def maxProfit( self, prices: List[int] ) -> int:
        ans = 0
        i = prices[0]
        
        for j in prices[ 1 : ]:
            if j < i:
                i = j
            else:
                ans = max( j - i, ans )
                
        return ans