from typing import *

def modifyMex( n: int, a: List[int] ) -> int:
    
    s = set( a )

    for i in range( 10 ** 10 ):
        if i not in s:
            if i + 2 in s:
                return -1
            elif i + 1 in s:
                return 1
            else:
                return 2
