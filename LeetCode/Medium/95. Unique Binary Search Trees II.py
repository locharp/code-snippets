class Solution:
    def generateTrees( self, n: int ) -> List[Optional[TreeNode]]:
        t = [ [ [ None ] ] * ( n + 1 ) ] + [ [ [] for p in range( n - q ) ] for q in range( n - 1 ) ]
        
        for i in range( 1, n ):
            for j in range( n - i + 1 ):
                for k in range( j + 1, j + i + 1 ):
                    for u in t[ k - j - 1 ][j]:
                        for v in t[ i - k + j ][k]:
                            t[i][j].append( TreeNode( k, u, v ) )
                            
        return [ TreeNode( i, j, k ) for i in range( 1, n + 1 ) for j in t[ i - 1 ][0] for k in t[ n - i ][i] ]