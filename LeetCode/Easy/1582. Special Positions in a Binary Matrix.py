class Solution:

    def numSpecial( self, mat: List[ List[int] ] ) -> int:
        
        n = len( mat[0] )
        p = [ 0 ] * n
        q =  [ 0 ] * n
        ans = 0

        for i in mat:
            o = -1

            for j in range( n ):
                if i[j] > 0:
                    p[j] += 1

                    if o < 0:
                        o = j
                    else:
                        o = 101

            if o > -1 and o < 101:
                q[o] += 1
        
        for i in range( n ):
            if p[i] == 1 and q[i] == 1:
                ans += 1

        return ans
