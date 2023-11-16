def leftRotationsOfArray( nums, queries ):
    
    ans = []
    m = len( nums )
    
    for query in queries:
        n = query % m
        
        ans.append( nums[ n : ] + nums[ : n ] )
        
    return ans
