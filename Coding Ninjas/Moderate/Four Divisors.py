from collections import Counter

def f( n ):    
    s = { 1, n }
    i = 2
    j = n
    
    while i < j:
        if n % i == 0:
            j = n // i
            s.add( i )
            s.add( j )
            
        i += 1
            
    return s



def sumFourDivisors( arr, n ):
    
    ans = 0
    c = Counter( arr )
    
    for i, j in c.items():
        s = f( i )
        
        if len( s ) == 4:
            ans += sum( s ) * j
        
    return ans
