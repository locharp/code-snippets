def nextGreater( arr,n ):
    
    a = []
    ans = [ -1 ] * n

    for i, j in enumerate( arr ):
        while len( a ) > 0 and arr[ a[-1] ] < j:
            ans[ a.pop() ] = j

        a.append( i )
            
    return ans
