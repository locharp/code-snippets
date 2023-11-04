def getAverage( n: int, q: int, arr: [int], queries: [ [int] ] ) -> [int]:
    
    ans = []
    
    for p in queries:
        if len( p ) < 3:
            arr.append( p[1] )
        else:
            ans.append( sum( arr[ p[1] - 1 : p[2] ] ) // ( p[2] - p[1] + 1 ) )

    return ans
