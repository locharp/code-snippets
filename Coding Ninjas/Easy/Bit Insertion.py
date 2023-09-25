def bitInsertion( x, y, a, b ):
    w = 32
    x = bin( x )[ 2 : ].rjust( w, "0" )
    y = bin( y )[ 2 : ]
    z = len( y )
    y = y.rjust( w, "0" )
    
    return int( x[ : min( w - z - a, w - b - 1 ) ] + y[ -max( b - a + 1, z ) : ] + x[ w - a : ], 2 )
