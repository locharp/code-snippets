from collections import *

def nestedRangesCount( ranges, n ):
    d = defaultdict( list )
    
    for i, j in ranges:
        d[i].append( j )
        
    a = sorted( d )
    p = [ 0 ] * n
    q = [ 0 ] * n
    for h in range( n ):
        i, j = ranges[h]
        
        for k in d[i]:
            if k < j:
                p[h] += 1
            elif k > j:
                q[h] += 1
                
        for m in a:
            if m <= i:
                continue
            elif m >= j:
                break
                
            for o in d[m]:
                if o <= j:
                    p[h] += 1
                    
        for m in a:
            if m >= i:
                break
                
            for o in d[m]:
                if o >= j:
                    q[h] += 1
                    
    return [ p, q ]