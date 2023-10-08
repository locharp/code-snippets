def numFollowingPattern( s ):
    n = len( s )
    a = [ 1 ]
    c = 2
    
    for i in range( n ):
        if s[i] == "I":
            a.append( c )
        else:
            j, d = i, a[i]
            
            while j > 0 and a[j] < a[ j - 1 ]:
                j -= 1
                
            for k in range( j, i + 1):
                a[k] += 1
    
            a.append( d )
        
        c += 1
        
    return "".join( map( str, a ) )
