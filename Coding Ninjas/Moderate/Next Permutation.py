from bisect import bisect_left

def nextPermutation( permutation, n ):
    
    m = permutation[ -1 ]
    a = []

    while len( permutation ) > 0:
        p = permutation.pop()
        j = bisect_left( a, p )
        
        if j < len( a ):
            permutation.append( a.pop( j ) )
            a.insert( j, p )
            return permutation + a

        a.insert( j, p )

    return a
