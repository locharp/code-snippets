def threePointer( X:list, Y:list, Z:list, ans = 2147483647 ):
    if len( X ) < 1 or len( Y ) < 1 or len( Z ) < 1:
        return ans
    
    m = max( X[0], Y[0], Z[0] )
    n = min( X[0], Y[0], Z[0] )
    ans = min( ans, m - n )
    
    if X[0] == n:
        X.pop( 0 )
    elif Y[0] == n:
        Y.pop( 0 )
    else:
        Z.pop( 0 )
        
    return threePointer( X, Y, Z, ans )
