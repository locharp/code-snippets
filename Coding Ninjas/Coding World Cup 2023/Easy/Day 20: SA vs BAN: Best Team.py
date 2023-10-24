from typing import *

def gun_devil( n: int, a: List[int] ) -> int:

    a.sort()
    a.pop( -2 )

    return sum( a )
