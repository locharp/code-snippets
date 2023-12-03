def f( a, s, i, j ):

    if j - i < 1:
        return True
    elif a[i][j] is not None:
        return a[i][j]

    if s[i] == s[j]:
        a[i][j] = f( a, s, i + 1, j - 1 )
        return a[i][j]
    else:
        a[i][j] = False
        return False


class Solution:

    def longestPalindrome( self, s: str ) -> str:
        
        a = [ [ None ] * len( s ) for i in range( len( s ) ) ]
        
        for i in range( len( s ) - 1, -1, -1 ):
            for j in range( len( s ) - i ):
                if f( a, s, j, j + i):
                    return s[ j : j + i + 1 ]
