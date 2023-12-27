def addAndSubtract( n: int, k: int ) -> List[int]:
    
    ans = [ n + 1 ]
    p = 2
    q = -1

    for i in range( k - 1 ):
        ans.append( ans[-1] + ( p * q ) )
        p += 1
        q *= -1

    return ans
