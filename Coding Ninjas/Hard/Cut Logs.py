import math

def cutLogs( k, n ):
    ans = math.log( n, 2 )
    
    if ans.is_integer():
        return math.ceil( ans ) + 1
    else:
        return math.ceil( ans )
