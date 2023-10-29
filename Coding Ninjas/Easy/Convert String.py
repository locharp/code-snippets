def convertString( str ):

    a = str.split()

    for i in range( len( a ) ):
        a[i] = a[i][0].upper() + a[i][ 1 : ]

    return " ".join( a )
