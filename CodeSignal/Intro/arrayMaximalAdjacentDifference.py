def solution( inputArray ):
    return max( abs( inputArray[i] - inputArray[ i - 1 ] ) for i in range( 1, len( inputArray ) ) )
