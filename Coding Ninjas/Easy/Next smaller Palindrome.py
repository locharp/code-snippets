def nextSmallerPalindrome( s ):
    
    if s == "11":
        return "9"
    elif int( s ) < 11:
        return str( int( s ) - 1 )
        
    n = len( s ) // 2
    m = len( s ) % 2
    
    if s[ n - 1 : : -1 ] < s[ n + m : ]:
        return s[ : n ] + s[ n - ( 1 - m ) : : -1 ]
    else:
        t = str( int( s[ : n + m ] ) - 1 )

        if len( t ) < n + m:
            return "9" * ( len( s ) - 1 )
            
        return t + t[ n - m : : -1 ]
