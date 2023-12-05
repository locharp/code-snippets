from collections import defaultdict

def f( a, g, s, t, v ):
    q = []

    for i in a:
        if len( i ) < 1:
            continue
            
        q.append( [] )

        for j in g[ i[-1] ]:
            if j == t:
                return i + [ j ]

            q.append( i + [ j ] )
            v.add( j )

    return f( q, g, s, t, v )



def shortestPath( edges, n, m, s, t ):
    
    g = defaultdict( list )

    for i, j in edges:
        g[i].append( j )
        g[j].append( i )

    return f( [ [ s ] ], g, s, t, set() )

