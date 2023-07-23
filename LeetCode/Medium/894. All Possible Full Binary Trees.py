class Solution:
    def allPossibleFBT( self, n: int ) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        dp = [ [ TreeNode() ] ] + [ [] for _ in range( n // 2) ]
        
        for k in range( 1, n // 2 + 1 ):
            for i in range( k ):
                j = k - i - 1
                
                for p in dp[i]:
                    for q in dp[j]:
                        dp[k].append( TreeNode( 0, p, q ) )
                        
        return dp[-1]