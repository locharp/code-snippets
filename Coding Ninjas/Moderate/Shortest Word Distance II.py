from collections import defaultdict

def minimumDistance( arr, book1, book2 ):
    
    d = defaultdict( set )

    for i, j in enumerate( arr ):
        d[j].add( i )

    return min( abs( j - i ) for i in d[book1] for j in d[book2] )
