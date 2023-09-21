def solveNQueens( n ):
    ans = []
    
    def f( n, a, ans ):
        m = len( a )
        
        if m == n:
            ans.append( [ 0 ] * ( n * n ) )
            
            for i in range( m ):
                ans[-1][ i * n + a[i] ] = 1
                
            return
        
        for j in range( n ):
            t = True
            
            for i in range( m ):
                if a[i] == j or m - i == abs( j - a[i] ):
                    t = False
                    break
                    
            if t:
                a.append( j )
                f( n, a, ans )
                a.pop()
                    
    f( n, [], ans )
    
    return ans