from typing import List, Tuple

def printAdjacency( n: int, m: int, edges: List[ Tuple[int, int] ] ) -> List[ List[int] ]:

    ans = [ [ i ] for i in range( n ) ]

    for i, j in edges:
        ans[i].append( j )
        ans[j].append( i )
        
    return ans
