class Solution:
    def gcdOfStrings( self, str1: str, str2: str ) -> str:
        p, q = len( str1 ), len( str2 )
        n = gcd( p, q)
        s = str1[ : n ]
        
        for i in range( n, p, n ):
            if s != str1[ i : i + n ]:
                return ""
            
        for i in range( 0, q, n ):
            if s != str2[ i : i + n ]:
                return ""
            
        return s
