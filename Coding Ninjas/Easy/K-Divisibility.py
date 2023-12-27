from typing import List

def kDivisibility( n: int, k: int, a: List[int] ) -> int:
    
    s = { i % k for i in a }
    s.discard( 0 )

    return len( s )
