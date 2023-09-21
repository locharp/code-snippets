class Solution:
    def kthGrammar( self, n: int, k: int, j: int = 0 ) -> int:
        if k < 9:
            return abs( j - int( "01101001"[ k - 1 ] ) )
        elif k > 2 ** n:
            return self.kthGrammar( n - 1, k - 2 ** n, 1 - j )
        else:
            return self.kthGrammar( n - 1, k, j )