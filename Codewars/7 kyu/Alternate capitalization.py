def capitalize( s ):
    
    s = list( s.lower() )
    ans = [ [ i for i in s ] for j in range( 2 ) ]
    
    for i in range( len( s ) ):
        ans[ i % 2 ][i] = ans[ i % 2 ][i].upper()
        
    for i in range( 2 ):
        ans[i] = "".join( ans[i] )
        
    return ans
