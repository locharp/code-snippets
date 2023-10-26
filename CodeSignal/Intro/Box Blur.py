def solution( image ):
    
    ans = []
    
    for i in range( 0, len( image ) - 2 ):
        ans.append( [] )
        
        for j in range ( 0, len( image[0] ) - 2 ):
            ans[-1].append( sum( sum( r[ j : j + 3 ] ) for r in image[ i : i + 3 ] ) // 9 )
            
    return ans
