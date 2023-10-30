def nextLargestPalindrome( s, length ):
    
    if length < 2:
        t = int( s )
        
        return str( t + ( 2 if t > 8 else 1 ) )
        
    g = length % 2
    h = length // 2
    
    if s[ h - 1 : : -1 ] > s[ -h : ]:
        return s[ : h ] + s[ h if g > 0 else h - 1 : : -1 ]

    h += g
    t = str( int( s[ : h ] ) + 1 )

    if len( t ) > h:
        return t[ : -g - 1 ] + t[ : : - 1]
    else:
        return t + ( t[ h - 2 : : -1 ] if g > 0 else t[ : : -1 ] )
