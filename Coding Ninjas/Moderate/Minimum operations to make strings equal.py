def minimumOperations(a, b):

    n = len( a )

    if n != len( b ):
        return -1

    m = n // 2
    ans = 0

    for i in range( m ):
        j = n - i - 1
        s = { a[i], a[j], b[i], b[j] }
        o = len( s )

        if o > 3:
            ans += 2
        elif o > 2:
            if a[i] == a[j]:
                ans += 2
            else:
                ans += 1
        elif a[i] == a[j] and b[i] != b[j] or a[i] != a[j] and b[i] == b[j]:
            ans += 1

    if n % 2 > 0 and a[m] != b[m]:
        ans += 1

    return ans
