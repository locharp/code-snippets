def nextLargestPalindrome( s, length ):
    
    if length < 2:
        t = int( s )
        
        return str( t + ( 2 if t > 8 else 1 ) )
        
    m = length % 2
    n = length // 2
    
    if s[ n - 1 : : -1 ] > s[ n + m : ]:
        return s[ : n ] + s[ n - ( 1 - m ) : : -1 ]
    else:
        t = str( int( s[ : n + m ] ) + 1 )

        if len( t ) > n + m:
            return "1" + "0" * ( len( s ) - 1 ) + "1" 
            
        return t + t[ n - m : : -1 ]
        
        
        
def nextLargestPalindrome2( s, length ):
    
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
