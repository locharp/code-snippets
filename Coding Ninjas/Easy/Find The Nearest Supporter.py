def prevSmall( arr, n ):
    
    ans = [ -1 ] * n
    a = []
    
    for i in range( n - 1, -1, -1 ):
        while len( a ) > 0 and arr[i] < arr[ a[-1] ]:
            ans[ a.pop( -1 ) ] = arr[i]
            
        a.append( i )
        
    return ans
