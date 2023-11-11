from typing import *

def distinctLeft( arr: List[int], n: int, k: int ) -> int:
    
    return len( set( sorted( arr )[ : -k ] ) )
