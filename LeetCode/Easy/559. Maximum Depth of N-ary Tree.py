class Solution:
    def maxDepth( self, root: 'Node', depth = 0 ) -> int:
        if root is None:
            return depth
        elif len( root.children ) > 0:
            return max( self.maxDepth( child, depth + 1 ) for child in root.children )
        else:
            return depth + 1