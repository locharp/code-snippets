from collections import defaultdict

def shortestPath( edges, n, m, s, t ):
    
    g = defaultdict( set )
    p = [ [ s ] ]
    v = { s }

    for i, j in edges:
        g[i].add( j )
        g[j].add( i )

    while len( p ) > 0:
        q = []

        for i in p:
            for j in g[ i[-1] ]:
                if j in v:
                    continue
                elif j == t:
                    return i + [ t ]
                else:
                    q.append( i + [ j ] )
                    v.add( j )

        p = q
