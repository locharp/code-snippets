from typing import *

def xAndY( x: int, y: int, a: List[int] ) -> int:
    
    for i in sorted( a ):
        if i >= x and i <= y:
            return i

    return -1
