from typing import List

def demonSlayer( n: int, a: int, b: int, x: List[int], y: List[int] ) -> int:
    
    return max( len( [ i for i in x if i == a ] ), len( [ i for i in y if i == b ] ) )
