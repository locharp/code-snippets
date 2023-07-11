class Solution:
    def distanceK( self, root: TreeNode, target: TreeNode, k: int ) -> List[int]:
        graph = collections.defaultdict( list )
        
        def build_graph( this ):
            if this.left is not None:
                graph[this.val].append( this.left.val )
                graph[this.left.val].append( this.val )
                build_graph( this.left )
                
            if this.right is not None:
                graph[this.val].append( this.right.val )
                graph[this.right.val].append( this.val )
                build_graph( this.right )
                
        build_graph( root )
        visited = set( [ target.val ] )
        to_visit = [ target.val ]
        ans = []
        
        while k > 0 and len( to_visit ) > 0:
            nexts = []
            
            for node in to_visit:
                for nxt in graph[node]:
                    if nxt not in visited:
                        visited.add( nxt )
                        nexts.append( nxt )
                
            to_visit = nexts
            k -= 1
        else:
            return to_visit
        
        return []