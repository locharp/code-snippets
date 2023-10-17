class UnionFind:
    
    def __init__( self, n ):
        
        self.parents = [ -1 ] * n
        self.max_size = n
        self.size = 0
        
        
        
    def find_roots( self, children ):
        
        parents = set( range( self.max_size ) ).difference( children )
            
        for parent in parents:
            self.parents[parent] = parent
            self.size += 1

        return parents
            
            
            
    def find_parent( self, child ):
        
        if self.parents[child] != child:
            self.parents[child] = self.find_parent( self.parents[child] )
            
        return self.parents[child]
        
        
        
    def union( self, child, parent ):
        parent = self.find_parent( parent )

        if self.parents[child] != -1:
            return False

        self.parents[child] = parent
        self.size += 1

        return True
        

        
class Solution:
    
    def validateBinaryTreeNodes( self, n: int, leftChild: List[int], rightChild: List[int] ) -> bool:
        
        union = UnionFind( n )
        children = set( leftChild + rightChild )
        children.discard( -1 )
        parents = union.find_roots( children )

        if len( parents ) != 1:
            return False

        while len( parents ) > 0:
            parent = parents.pop()
            
            for child in [ leftChild[parent], rightChild[parent] ]:
                if child != -1:
                    if not union.union( child, parent ):
                        return False
                    else:
                        parents.add( child )
                    
        return union.size == n
