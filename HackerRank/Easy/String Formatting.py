def print_formatted( number ):
    
    w = len( bin( number ) ) - 2
    
    for i in range( 1, number + 1 ):
        print( f"{i:>{w}} {i:>{w}o} {i:>{w}X} {bin( i )[ 2 : ]:>{w}}" )
