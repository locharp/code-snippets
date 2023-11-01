def f( d, root ):
    
    if root is None:
        return

    d[root.val] += 1
    f( d, root.left )
    f( d, root.right )





class Solution:

    def findMode( self, root: Optional[TreeNode] ) -> List[int]:

        d = defaultdict( int )
        f( d, root )
        a = sorted( [ ( j, i ) for i, j in d.items() ], reverse = True )
        ans = [ a[0][1] ]

        for i, j in a[ 1 : ]:
            if i == a[0][0]:
                ans.append( j )
            else:
                break

        return ans
