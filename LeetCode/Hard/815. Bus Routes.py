class Solution:

    def f( self, a, c, d, e, n, o, t ):

        if t in o:
            return n
            
        m = set()

        for i in o:
            for j in e[i]:
                if j in d:
                    continue

                d.add( j )

                for k in a[j]:
                    if k in c:
                        continue

                    c.add( k )
                    m.add( k )

        if len( m ) < 1:
            return -1

        return self.f( a, c, d, e, n + 1, m, t )



    def numBusesToDestination( self, routes: List[ List[int] ], source: int, target: int ) -> int:

        e = defaultdict( set )

        for i in range( len( routes ) ):
            for j in routes[i]:
                e[j].add( i )
        
        ans = self.f( routes, { source }, set(), e, 0, { source } , target )

        return ans if ans < 501 else -1
