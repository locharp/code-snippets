def possibleNumbers( n, m, digits ):
    ans = 0
    t = str( n )
    o = len( t )
    s = list( map( str, digits ) )
    r = len( [ i for i in s if i < t[0] ] )
    
    if t[0] in s:
        for i in range( 1, o ):
            if i == o - 1:
                ans += len( [ j for j in s if j <= t[i] ] )
                break
            else:
                ans += len( [ j for j in s if j < t[i] ] ) * m ** ( o - i - 1 )
            
            if t[i] not in s:
                break
                
    ans += r * ( m ** ( o - 1 ) )
    
    for i in range( 1, o ):
        ans += m ** i
        
    return ans
