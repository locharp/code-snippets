def minCostToDestination( matrix, n, m, x, y ):
    
    p = [ ( 0, 0 ) ]
    ans = 0
    a = [ [ False ] * m for i in range( n ) ]
    a[0][0] = True
    d = [ 1, -1 ]

    while len( p ) > 0:
        q = p

        for i, j in p:
            if i == x and j == y:
                return ans
                            
            for k in range( j - 1, -1, -1 ):
                if matrix[i][k] < 1 or a[i][k]:
                    break
                
                a[i][k] = True
                q.append( ( i, k ) )
            
            for k in range( j + 1, m ):
                if matrix[i][k] < 1 or a[i][k]:
                    break
                
                a[i][k] = True
                q.append( ( i, k ) )
            
        p = []
        ans += 1

        for r, s in q:
            for k in d:
                o = r + k
                
                if o >= 0 and o < n and matrix[o][s] > 0 and not a[o][s]:
                    a[o][s] = True
                    p.append( ( o, s ) )
                    
    return -1
