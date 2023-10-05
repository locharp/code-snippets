def maxProfit( prices, n ):
    a = [ 2147483647, 0, 2147483647, 0 ]
    
    for i in prices:
        a[0] = min( a[0], i )
        a[1] = max( a[1], i - a[0] )
        a[2] = min( a[2], i - a[1] )
        a[3] = max( a[3], i - a[2] ) 
        
    return a[3]
