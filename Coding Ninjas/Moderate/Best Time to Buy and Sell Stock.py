def maximumProfit( prices ):
    ans = 0
    curr = float( "inf" )

    for price in prices:
        if price > curr:
            ans = max( ans, price - curr )
        else:
            curr = price

    return ans
