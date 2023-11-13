class Solution:

    def sortVowels( self, s: str ) -> str:
        
        a = []
        c = []
        
        for i, j in enumerate( s ):
            if j in "AEIOUaeiou":
                a.append( i )
                c.append( j )
                
        c.sort()
        t = list( s )

        for i, j in enumerate( a ):
            t[j] = c[i]

        return "".join( t )
