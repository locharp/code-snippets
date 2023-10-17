from sortedcontainers import SortedList

def nextPermutation( permutation, n ):
    
    m = permutation[ -1 ]
    a = SortedList()

    while len( permutation ) > 0:
        k = permutation.pop()

        for i in range( len( a ) ):
            if a[i] > k:
                permutation.append( a.pop( i ) )
                a.add( k )
                permutation.extend( a )

                return permutation

        a.add( k )

    return a
