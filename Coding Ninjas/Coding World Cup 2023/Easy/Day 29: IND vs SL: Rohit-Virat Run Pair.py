def findPair( x: int, y: int ) -> list:

    if y > x or x % 2 != y % 2:
        return [ -1, -1 ]

    return [ ( x + y ) // 2, ( x - y + 1 ) // 2 ]
