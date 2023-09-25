def findDoubleStrings( str ):
    n = len( str )
    d = defaultdict( set )
    c = set()
    
    for i in range( n ):
        for j in range( i + 1, n + 1 ):
            if i + i - j in d[ str[ i : j ] ]:
                c.add( str[ i : j ] )
                
            d[ str[ i : j ] ].add( i )
            
    return len( c )
