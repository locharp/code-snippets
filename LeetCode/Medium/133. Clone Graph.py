"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    
    def __init__( self ):
        
        self.d = {}
        
        
        
    def cloneGraph( self, node: Optional['Node'] ) -> Optional['Node']:
        
        if node is None:
            return None
        
        self.d[node.val] = Node( node.val )
        
        for neighbor in node.neighbors:
            if neighbor.val not in self.d:
                self.cloneGraph( neighbor )
                
            self.d[node.val].neighbors.append( self.d[neighbor.val] )
                
        return self.d[node.val]
