def directionGame( n: int, s: str ) -> str:

    d = [ "NORTH", "WEST", "SOUTH", "EAST" ]
    x = s.count( "1" ) * 2 - n

    return d[ x % 4 ]
