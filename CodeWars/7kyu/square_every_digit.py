def square_digits( num ):
    return int( "".join( map( lambda i: str( int( i ) ** 2 ), str( num ) ) ) )