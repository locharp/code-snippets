from bisect import bisect_left

def findMaxEnvelopes( height, width, n ):
    
    a = sorted ( zip( height, width ), key = lambda x: ( x[0], -x[1] ) )
    ans = [ a[0][1] ]

    for i, j in a:
        if j > ans[-1]:
            ans.append( j )
        else:
            ans[ bisect_left( ans, j ) ] = j

    return len( ans )
