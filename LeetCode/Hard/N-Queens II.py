class Solution:
    def totalNQueens( self, n: int ) -> int:
        
        def f( n, a ):
            m = len( a )
            
            if m == n:
                return 1
            
            c = 0
            
            for i in range( n ):
                t = True
                
                for j in range( m ):
                    if i == a[j] or m - j == abs( i - a[j] ):
                        t = False
                        break
                        
                if t:
                    a.append( i )
                    c += f( n, a )
                    a.pop()
                    
            return c
        
        return f( n, [] )
