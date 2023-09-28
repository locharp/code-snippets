def maximumBinaryString( str ):
    m = str.count( "1" )
    n = len( str )
    o = n - m
    
    if o > 1:
        p = str.index( "0" )
        return "1" * ( o + p - 1 ) + "0" + "1" * ( n - o - p )
    else:
        return str
