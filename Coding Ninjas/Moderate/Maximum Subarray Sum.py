def maxSubarraySum(arr, n) :

    c = m = 0

    for i, j in enumerate( arr ):
        c += j

        if c > m:
            m = c
        elif c < 0:
            c = 0

    return m


