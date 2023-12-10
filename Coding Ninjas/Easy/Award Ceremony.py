from typing import *

def getTotalRewards( n: int, arr: List[int] ) -> int:
    
    return len( { i for i in arr if i > 0 } )
