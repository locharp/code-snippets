from functools import reduce

ans = 0
    
def cal( m, n ):
    
    nonlocal ans
    
    need = m - n + 1 if m >= n else 0
    ans += need
        
    return n + need
    
    
    
def solution( inputArray ): 
    reduce( cal, inputArray )
    
    return ans
