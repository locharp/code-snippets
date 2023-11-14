def f( d, i, j ):
    a = []
    t = 0

    for k in d[j]:
        t = min( d[i][j], d[j][k] )
        
        if i != k:
            if k not in d[i]:
                d[i][k] = t
            else:
                d[i][k] += t

        if d[j][k] > t:
            d[j][k] -= t
        else:
            a.append( ( j, k ) )

        if d[i][j] > t:
            d[i][j] -= t
        else:
            a.append( ( i, j ) )

        break

    for p, q in a:
        del d[p][q]

    return t > 0



def minCashFlow( money, n ):

    d = { i: {} for i in range( n ) }

    for i in range( n ):
        for j in range( n ):
            if money[i][j] > 0 and money[j][i] > 0:
                t = min( money[i][j], money[j][i] )
                money[i][j] -= t
                money[j][i] -= t
                
    for i in range( n ):
        for j in range( n ):
            if money[i][j] > 0:
                d[i][j] = money[i][j]

    t = True

    while t:
        t = False

        for i in range( n ):
            for j in range( n ):
                if j in d[i] and len( d[j] ) > 0:
                    if f( d, i, j ):
                        t = True

    return sum( sum( i.values() ) for i in d.values() )
