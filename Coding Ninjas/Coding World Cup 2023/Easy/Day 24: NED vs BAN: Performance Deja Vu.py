def deja_vu(n: int, w: List[int], k: int) -> int:
    
    a = w[ : 1 ]
    s = set()

    for i in w[ 1 : ]:
        a.append( a[-1] + i )

    for i in range( len( a ) ):
        for j in s:
            if abs( a[i] - j ) <= k:
                return i + 1

        s.add( a[i] )

    return -1
