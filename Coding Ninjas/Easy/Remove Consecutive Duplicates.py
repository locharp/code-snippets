def removeConsecutiveDuplicates( string ):

    return string[0] + "".join( string[i] for i in range( 1, len( string ) ) if string[i] != string[ i - 1 ] )
