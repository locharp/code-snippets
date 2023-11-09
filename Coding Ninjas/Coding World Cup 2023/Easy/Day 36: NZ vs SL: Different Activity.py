def makeInnocent( a: str ) -> int:
    
    ans = 0
    i = 1
    t = False

    while i < len( a ):
        if a[i] == a[ i - 1 ]:
            if t:
                ans += 1
                i += 1
                t = False
            else:
                t = True

        i += 1

    return ans
