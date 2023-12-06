def maximumProfit( prices ):
    ans = 0
    curr = float( "inf" )

    for price in prices:
        if price > curr:
            ans = max( ans, price - curr )
        else:
            curr = price

    return ans



# 2
def maximumProfit( prices ):
    
    a = sorted( ( j, i ) for i, j in enumerate( prices ) )
    ans = 0

    for i, j in enumerate( prices ):
        while len( a ) > 0:
            if a[-1][1] <= i:
                a.pop()
            else:
                ans = max( ans, a[-1][0] - j )
                break
                
    return ans
