class Solution:
    def solveNQueens( self, n: int ) -> int:
        
        def f( n, a, d ):
            m = len( a )
            
            if m == n:
                d.append( a.copy() )
                return
            
            for i in range( n ):
                t = True
                
                for j in range( m ):
                    if i == a[j] or m - j == abs( i - a[j] ):
                        t = False
                        break
                        
                if t:
                    a.append( i )
                    f( n, a, d )
                    a.pop()
                    
        d = []
        f( n, [], d )
        ans = []
        
        for i in d:
            ans.append( [] )
            
            for j in i:
                ans[-1].append( "." * j + "Q" + "." * ( n - j - 1 ) )
                
        return ans
