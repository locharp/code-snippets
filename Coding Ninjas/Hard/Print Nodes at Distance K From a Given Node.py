from collections import defaultdict

def printNodesAtDistanceK( root, target, K ):

    d = defaultdict( list )
    q = [ root ]

    while len( q ) > 0:
        p = q.pop()

        if p.left is not None:
            q.append( p.left )
            d[p].append( p.left )
            d[p.left].append( p )

        if p.right is not None:
            q.append( p.right )
            d[p].append( p.right )
            d[p.right].append( p )

    q = [ target ]
    s = { target }

    while K > 0:
        p = []

        for i in q:
            for j in d[i]:
                if j not in s:
                    s.add( j )
                    p.append( j )

        q = p
        K -= 1
    
    return q
