def binaryGap( num ):
    
    ans = 0
    n = -1000
    
    for i in bin( num )[ 2 : ]:
        if i == "0":
            n += 1
        else:
            ans = max( ans, n )
            n = 1

    return ans
