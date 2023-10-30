def nextLargestPalindrome( s, length ):
    
    if length < 2:
        t = int( s )

        if t < 9:
            return str( t + 1 )
        else:
            return str( t + 2 )

    g = length % 2
    h = length // 2
    
    if g > 0:
        if s[ h - 1 : : -1 ] > s[ -h : ]:
            return s[ : h ] + s[ h : : -1 ]
    elif s[ h - 1 : : -1 ] > s[ -h : ]:
        return s[ : h ] + s[ h - 1 : : -1 ]

    h += g
    t = str( int( s[ : h ] ) + 1 )

    if len( t ) > h:
        return t[ : h ] + ( "0" if g < 1 else "" ) + t[ : h ][ : : - 1]
    elif g > 0:
        return t + t[ : -1 ][ : : -1 ]
    else:
        return t + t[ : : -1 ]
