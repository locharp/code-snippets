from collections import *

from typing import *

def aliceStrings( K: int, A: str, B: str ) -> str:
    
    if len( A ) != len( B ):
        return "No"
    
    return "No" if sum( i for i in ( Counter( A ) - Counter( B ) ).values() if i > 0 ) > K else "Yes"
