from collections import *

def f( d, m, n, o ):
    
    if n == m:
        return [ o ]
        
    for i in d[o]:
        d[o].remove( i )
        d[i].remove( o )
        
        ans = f( d, m, n + 1, i )
        
        if ans != -1:
            return [ o ] + ans
        
        d[o].append( i )
        d[i].append( o )
        
    return -1
    
    
def printEulerPath( n, edgeList ):
    
    d = defaultdict( list )
    
    for i, j in edgeList:
        d[i].append( j )
        d[j].append( i )
        
    for i in range( n ):
        ans = f( d, len( edgeList ), 0, i )
        
        if ans != -1:
            return ans
    
    return [ -1 ]
