def f( a, s, i, j ):

    if j - i < 1:
        return True
    elif a[i][j] is not None:
        return a[i][j]

    if s[i] == s[j]:
        return f( a, s, i + 1, j - 1 )
    else:
        return False
        


class Solution:

    def longestPalindrome( self, s: str ) -> str:
        
        a = [ [ None ] * len( s ) for i in range( len( s ) ) ]
        ans = [ 0, 0 ]

        for i in range( len( s ) ):
            for j in range( len( s ) - i ):
                a[j][ j + i ] = f( a, s, j, j + i )

        for i in range( len( s ) - 1, -1, -1 ):
            for j in range( len( s ) - i ):
                if a[j][ j + i ]:
                    return s[ j : j + i + 1 ]
