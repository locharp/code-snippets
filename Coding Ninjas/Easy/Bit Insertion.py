def bitInsertion( x, y, a, b ):
    x = bin( x )[ 2 : ].rjust( b, "0" )
    y = bin( y )[ 2 : ].rjust( b - a + 1, "0" )
    
    return int( x[ : -b - 1] + y + x[ -a : ], 2 )
