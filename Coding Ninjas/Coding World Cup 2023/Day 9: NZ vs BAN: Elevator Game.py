def minimumTime( x: int, y: int, z: int ) -> int:

    return 30 + max( ( j - 1 ) // 2 * 3 + i for i, j in enumerate( [ x, y, z ] ) )
