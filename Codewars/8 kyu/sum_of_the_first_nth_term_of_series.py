def series_sum( n ):
    return "{:.2f}".format( sum( 1 / ( 1 + 3 * i ) for i in range( n ) ) )