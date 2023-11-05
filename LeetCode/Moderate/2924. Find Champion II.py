class Solution:
    
    def findChampion( self, n: int, edges: List[ List[int] ]) -> int:
        
        s = { i for i in range( n ) } - { j for i, j in edges }
        
        return s.pop() if len( s ) < 2 else -1
