def g( s, i, j ):
    
    if s[ i - j : i + 1 ] == s[ i : i + j + 1 ][ : : -1 ]:
        return f( s, i, j + 1 )

    return j



def f( s, i, j ):
    
    if i - j < 0 or i + j >= len( s ) or s[ i + j ] != s[ i - j ]:
        return j - 1

    return f( s, i, j + 1 )

    

def manacherAlgo( s: str ) -> str:

    p = q = 0
    s = "$".join( list( s ) )
    a = [ 0 ] * len( s )
    
    for i in range( len( s ) ):
        
        a[i] = g( s, i, q )
        
        if i % 2 < 1:
            if a[i] % 2 > 0:
                a[i] -= 1
        else:
            if a[i] % 2 < 1:
                a[i] -= 1

        if a[i] > q:
            q = a[i]
            p = i
            
    return s[ p - q : p + q + 1 ].replace( "$", "" )
