from itertools import permutations

def f( d, i ):
    if d[i] != i:
        d[i] = f( d, d[i] )
        
    return d[i]



def minMaxValue( exp: str ) -> Tuple[int, int]:
    
    m, n = float( "-inf" ), float( "inf" )
    c = []
    i = j = 0
    ans = set()
    
    while j < len( exp ):
        if exp[j] == "+" or exp[j] == "*":
            c.append( exp[ i: j ] )
            i = j
            
        j += 1
            
    c.append( exp[ i : j ] )
    c[0] = "+" + c[0]
    o = len( c )
    
    for i in permutations( range( 1, o ) ):
        e = [ i for i in c ]
        d = { i: i for i in range( o ) }
        
        for j in i:
            p = f( d, j - 1 )
            q = f( d, j )
            
            if e[q][0] == "+":
                e[p] = e[q] = e[p][0] + str ( int( e[p][ 1 : ] ) + int( e[q][ 1 : ] ) )
            else:
                e[p] = e[q] = e[p][0] + str ( int( e[p][ 1 : ] ) * int( e[q][ 1 : ] ) )
            
            d[j] = p
            
        ans.add( int( e[0][ 1 : ] ) )
     
    return ( min( ans ), max( ans ) )
