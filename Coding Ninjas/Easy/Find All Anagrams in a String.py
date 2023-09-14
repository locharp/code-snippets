from collections import Counter

def findAnagramsIndices(str, ptr, n, m):
    c = Counter( ptr )
    ans = []
    
    for i in range( n - m + 1):
        if Counter( str[ i : i + m ] ) == c:
            ans.append( i )
            
    return ans