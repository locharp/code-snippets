class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def f( root, a ):
    if root.left != None:
        f( root.left, a)
        
    a.append( root.data )
    
    if root.right != None:
        f( root.right, a )
        
def flatten( root ):
    a = []
    f( root, a )
    
    root = TreeNode( a[0] )
    curr = root
    
    for i in a[ 1 : ]:
        curr.right = TreeNode( i )
        curr = curr.right
        
    return root