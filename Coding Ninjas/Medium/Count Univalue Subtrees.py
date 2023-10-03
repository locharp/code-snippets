class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        


def countUnivalTrees( root ):
    
    if root is None:
        return 0
    
    

    def f( root, ans ):
        
        m = root.left is None or f( root.left, ans ) and root.data == root.left.data 
        n = root.right is None or f( root.right, ans ) and root.data == root.right.data
        
        if m and n:
            ans[0] += 1
        
            return True
        else:
            return False
        
        
        
    ans = [ 0 ]
    f( root, ans )
    
    return ans[0]
