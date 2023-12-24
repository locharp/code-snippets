def canCompleteChallenges( arr, mat ):
    
    a = [ 0 ] * len( arr )
    ans = [ 0 ] * len( mat )

    for i in range( len( arr ) ):
        a[i] = a[ i - 1 ] + arr[ i ]
    
    for m in range( len( mat ) ):
        i, j, k = mat[m]
        
        if a[i] > j and ( i < 1 or a[ i - 1 ] < ( j + 1 ) * k ):
            ans[m] = 1

    return ans
