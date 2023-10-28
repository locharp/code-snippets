def merge_the_tools( string, k ):
    
    n = len( string )
    
    for i in range( 0, n, k ):
        u = []
        
        for j in range( i, i + k ):
            if string[j] not in u:
                u.append( string[j] )
                
        print( "".join( u ) )
