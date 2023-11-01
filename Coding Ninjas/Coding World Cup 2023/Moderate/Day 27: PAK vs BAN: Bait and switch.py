def baitAndSwitch( n: int, a: list, k: int, m: int ) -> int:
    
    ans = i = 0
    a.sort()
    n -= 1

    while i <= n and k > 0:
        p = abs( m - a[i] )
        q = abs( m - a[n] )

        if p > q:
            ans += p
            i += 1
        else:
            ans += q
            n -= 1

        k -= 1
    
    return ans
