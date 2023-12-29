def minimumDistance( arr, n, x, y ):
    
    ans = i = j = n

    for k in range( n ):
        if arr[k] == x:
            i = k
            ans = min( ans, abs( i - j ) )
        elif arr[k] == y:
            j = k
            ans = min( ans, abs( i - j ) )

    if i == n or j == n:
        return -1
    else:
        return ans
