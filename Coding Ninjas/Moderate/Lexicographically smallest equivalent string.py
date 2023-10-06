from string import ascii_lowercase

def f( p, d ):
    if d[p] != p:
        d[p] = f( d[p], d )
        
    return d[p]



def g( p, q, d ):
    d[p] = f( p, d )
    d[q] = f( q, d )
    
    if d[p] > d[q]:
        d[ d[p] ] = d[q]
    else:
        d[ d[q] ] = d[p]
        
        
        
def smallestString( s, t, st ):
    d = { i: i for i in ascii_lowercase }
    
    for i in range( len( s ) ):
        g( s[i], t[i], d )
        
    return "".join( f( i, d ) for i in st )
