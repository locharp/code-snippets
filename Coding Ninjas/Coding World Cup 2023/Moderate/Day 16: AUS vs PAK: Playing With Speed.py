from typing import *

def f( x, k, s ):

    if k < 1:
        return

    p = ( x + 1 ) // 2
    q = ( x - 1 ) * 2

    s.add( p )
    s.add( q )
    f( p, k - 1, s )
    f( q, k - 1, s )



def playingWithSpeed( x: int, k: int ) -> int:

    s = { x }
    f( x, k, s )
    s.discard( 0 )

    return len( s )
