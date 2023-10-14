def multiplication_table( size ):

    size += 1
    
    return [ [ i * j for j in range( 1, size ) ] for i in range( 1, size ) ]
