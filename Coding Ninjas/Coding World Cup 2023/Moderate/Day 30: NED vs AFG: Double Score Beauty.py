def doubleBeauty( k: int, a: List[int] ) -> int:
    
    return sum( sorted( a )[ -k : ] ) * 2
