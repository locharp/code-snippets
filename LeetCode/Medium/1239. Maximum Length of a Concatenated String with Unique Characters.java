class Solution:

    def maxLength( self, arr: List[str] ) -> int:
        
        dp = [ set() ]

        for i in arr:
            s = set( i )

            if len( i ) > len( s ):
                continue

            for j in dp:
                t = set( j )

                if s.isdisjoint( t ):
                    dp.append( s | t )

            dp.append( s )

        return max( len( s ) for s in dp )
