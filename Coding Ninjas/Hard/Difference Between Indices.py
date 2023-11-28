from typing import *

def maxIndexDiff( arr: List[int], n: int ):
    
    for i in range( 1, n - 1 ):
        for j in range( 1, i + 1 ):
            if arr[ i - j ] < arr[-j]:
                return n - i
            
    return -1
