from functools import *

def sumOfKxKMatrices( arr: list, k: int ):
    
    @cache
    def f( i, j ):
        
        return sum( arr[i][ j : j + k ] )
    
    
    
    def g( i, j ):
        
        return sum( f( i, j ) for i in range( i, i + k ) )
    
    
    
    n = len( arr )
    ans = []
    
    for i in range( n - k + 1 ):
        ans.append( [] )
        
        for j in range( n - k + 1 ):
            ans[i].append( g( i, j ) )
            
    return ans
