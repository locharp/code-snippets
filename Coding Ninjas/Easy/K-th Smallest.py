def kSmallest( n, m, k, mat ):
    ans = mat.pop()
    
    for row in mat:
        ans = sorted( p + q for p in row for q in ans )[ : k ]
        
    return ans[-1]