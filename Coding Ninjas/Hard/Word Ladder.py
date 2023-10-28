from functools import lru_cache

def wordLadder( begin, end, dict ):
    
    def f( p, q, m ):

        if p == q:
            return m

        n = 2147483647

        for i in range( len( dict ) ):
            if a[i]:
                continue
                
            if g( p, dict[i] ):
                a[i] = True
                n = min( n, f( dict[i], q, m + 1 ) )
                a[i] = False
                    
        return n



    def g( x, y ):
        t = True

        for i in range( len( x ) ):
            if x[i] != y[i]:
                if t:
                    t = False
                else:
                    return t

        return True



    a = [ False ] * len( dict )
    ans = f( begin, end, 1 )

    return ans if ans < 2147483647 else -1
