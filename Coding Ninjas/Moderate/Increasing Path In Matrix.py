def longestIncreasingPath( mat, n, m, o = 1, p = 0, q = 0, a = None ):

    if a is None:
        a = [ [ True ] * m for i in range( n ) ]

    ans = o
    r = p + 1
    s = q + 1

    if r < n and mat[r][q] > mat[p][q] and a[r][q]:
        a[r][q] = False
        ans = longestIncreasingPath( mat, n, m, o + 1, r, q, a )

    if s < m and mat[p][s] > mat[p][q] and a[p][s]:
        a[p][s] = False
        ans = max( ans, longestIncreasingPath( mat, n, m, o + 1, p, s, a ) )

    return ans
