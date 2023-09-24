def maxExtraCheese( n: int, k: int, l: List[int], b: List[int] ) -> int:
    a = []
    
    for i in range( n ):
        a.append( max( l[i], b[i] ) )
        
    return sum( sorted( a )[ n - k : ] ) * 2