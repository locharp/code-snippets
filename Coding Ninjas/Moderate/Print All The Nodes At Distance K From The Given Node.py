from collections import defaultdict

def f( root, d, p ):
    
    if root is None:
        return
    
    d[p].append( root.data )
    d[root.data].append( p )
    f( root.left, d, root.data )
    f( root.right, d, root.data )
    


def kDistance( root, target, k ):

    if root is None:
        return []
        
    d = defaultdict( list )
    f( root.left, d, root.data )
    f( root.right, d, root.data )
    p = [ target ]
    s = { target }

    for j in range( k ):
        q = []

        while len( p ) > 0:
            for i in d[ p.pop() ]:
                if i not in s:
                    s.add( i )
                    q.append( i )

        p = q

    return p
