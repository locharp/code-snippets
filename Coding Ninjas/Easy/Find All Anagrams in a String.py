from collections import Counter

def findAnagramsIndices(str, ptr, n, m):
    c = Counter( ptr )
    ans = []
    
    for i in range( n - m + 1):
        if Counter( str[ i : i + m ] ) == c:
            ans.append( i )
            
    return ans



# 2
from collections import Counter

def findAnagramsIndices( str, ptr, n, m ):
    
    c = Counter( ptr )
    d = Counter( str[ : m ] )
    ans = []
    i = 0
    
    if c == d:
        ans.append( i )
        
    for ch in str[ m : ]:
        d[ str[i] ] -= 1
        d[ch] += 1
        
        if d[ str[i] ] < 1:
            del d[ str[i] ]
        
        i += 1
        
        if c == d:
            ans.append( i )
                        
    return ans
