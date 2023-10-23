from typing import *

def nines( n: int, a: List[int], k: int ) -> int:
    
    return 1 if a.count( 9 ) >= k else 0
