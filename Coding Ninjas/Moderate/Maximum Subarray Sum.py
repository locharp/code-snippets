def maxSubarraySum( arr, n ):
    
    c = m = 0

    for i in arr:
        c += i

        if c > m:
            m = c
        elif c < 0:
            c = 0

    return m
