def differentBitsSumPairwise( arr, n ):
    ans = 0
    
    for i in range( n ):
        for j in range( i + 1, n ):
            ans += bin( arr[i] ^ arr[j] ).count( "1" ) * 2
            
    return ans % 1000000007