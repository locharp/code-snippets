from typing import *
from collections import Counter

def replaceElements( a: List[int] ) -> int:
  
    c = len( [ i for i in Counter( a ).values() if i % 2 == 1 ] )

    return c // 2 if c % 2 == 0 else -1
