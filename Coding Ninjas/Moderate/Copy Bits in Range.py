def copyBitsInRange( a: int, b: int, x: int, y: int ) -> int:

    p = list( bin( a )[ 2 : ] )
    o = len( p )
    q = list( bin( b )[ 2 : ].zfill( o ) )

    for i in range( -x, max( -y, -o ) - 1, -1 ):
        if p[i] == "1":
            q[i] = "1"

    return int( "".join( q ), 2 )
