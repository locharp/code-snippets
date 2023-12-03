def f( a, s, i, j ):

    if i >= j:
        a[i][j] = True
        return True
    elif a[i][j] != None:
        return a[i][j]

    if s[i] == s[j]:
        a[i][j] = f( a, s, i + 1, j - 1 )
        return a[i][j]
    else:
        a[i][j] = False
        return False



def longestPalinSubstring( str: str ) -> str:
    
    n = len( str )
    a = [ [ None ] * n for i in range( n ) ]
    
    for i in range( n - 1, -1, -1 ):
        for j in range( n - i ):
            if f( a, str, j, j + i ):
                return str[ j : j + i + 1 ]
