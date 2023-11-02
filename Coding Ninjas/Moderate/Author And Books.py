from string import ascii_uppercase

def arrangeAuthors( s ):
    
    A = "A" + ascii_uppercase
    a = []

    for i in range( len( s ) ):
        a.append( str( i + 1 ) + ". " + s[i][0] )

        for j in range( 1, len( s[i] ) ):
            a.append( A[j] + ". " + s[i][j] )

    return a
