from itertools import combinations

def pwset( v ):
    
    ans = []
    
    for i in range( len( v ) + 1 ):
        ans += combinations( v , i )
        
    return ans
