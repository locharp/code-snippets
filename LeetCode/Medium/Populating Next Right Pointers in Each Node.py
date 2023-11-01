class Solution:
    
    def __init__( self ):
        
        self.a = []
    
    
    
    def f( self, root, i ):
    
        if root is None:
            return
        
        if i >= len( self.a ):
            self.a.append( [])
        
        self.a[i].append( root )
        self.f( root.left, i + 1 )
        self.f( root.right, i + 1 )
        
        
    
    def connect( self, root: 'Optional[Node]', i = 0 ) -> 'Optional[Node]':
        
        self.f( root, 0 )
        
        for i in self.a:
            for j in range( 1, len( i ) ):
                i[ j - 1 ].next = i[j]
                
        return root
