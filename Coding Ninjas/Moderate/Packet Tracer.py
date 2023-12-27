from collections import defaultdict

def willPacketReach( n: int, m: int, edges: List[ List[int] ] ) -> int:
    
    o = n - 1
    d = defaultdict( set )
    s = { 0: -1 }
    v = set()
    
    for i, j in edges:
        d[i].add( j )
        d[j].add( i )

    while len( s ) > 0:
        if o in s:
            return 1

        v.update( s )
        t = defaultdict( list )

        for i, j in s.items():
            for k in d[i]:
                if k != j and k not in v:
                    t[k].append( i )

        s = { i: j[0] for i, j in t.items() if len( j ) < 2 }

    return 0
