def f( a, d, m ):
    if len( a ) == m:
        return a
        
    for i in d[ a[-1] ]:
        d[ a[-1] ].remove( i )
        d[i].remove( a[-1] )
        a.append( i )
        
        
        ans = f( a, d, m )
        
        if ans[0] != -1:
            return ans
        
        a.pop()
        d[ a[-1] ].append( i )
        d[i].append( a[-1] )
        
    return [ -1 ]
    
    
def printEulerPath( n, edgeList ):
    
    d = defaultdict( list )
    
    for i, j in edgeList:
        a[j].append( i )
        d[i].append( j )
        d[j].append( i )
        
    for i in range( n ):
        ans = f( [ i ], d, len( edgeList ) + 1 )
        
        if ans[0] != -1:
            return ans
    
    return [ -1 ]
