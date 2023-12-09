def longestMountain( arr, n ):
    
    ans = i = j = 0
    o = arr[0]

    for k in arr[ 1 : ]:
        if k > o:
            if j > 0:
                ans = max( ans, i + j )
                j = 0
                i = 2
            elif i > 0:
                i += 1
            else:
                i = 2
        elif k < o:
            if i > 0:
                j += 1
        else:
            if j > 0:
                ans = max( ans, i + j )
                
            i = j = 0

        o = k
        
    if j > 0:
        ans = max( ans, i + j )

    return ans
    




# 2
def longestMountain( arr, n ):

    i = m = 0
    j = 1
    p = q = False

    while j < n:
        while j < n and arr[j] > arr[ j - 1 ]:
            j += 1
            p = True
            
        while p and j < n and arr[j] < arr[ j - 1 ]:
            j += 1
            q = True

        if p and q:
            m = max( m, j - i )
            j -= 1

        p = q = False
        i = j
        j += 1

    if p and q:
        m = max( m, j - i )

    return m
