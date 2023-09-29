def detectOdd(n, nums):
    d = Counter( nums )
    c = sorted( d )
    c.sort( key = lambda x: d[x] )
    
    return c[ : 2 ]
