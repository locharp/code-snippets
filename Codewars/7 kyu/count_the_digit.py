def nb_dig( n, d ):
    s = ""
    
    for i in range( n + 1 ):
        s += str( i ** 2 )
        
    return s.count( str( d ) )
