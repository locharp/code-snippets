# Following is the structure of BinaryTree Node
class BinaryTreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None




def identicalTrees( root1: BinaryTreeNode, root2:BinaryTreeNode ) -> bool:
    
    if root1.data != root2.data:
        return False
        
    if root1.left == None:
        if root2.left != None:
            return False
    elif root2.left == None:
        return False
    else:
        if not identicalTrees( root1.left, root2.left ):
            return False

    if root1.right == None:
        if root2.right != None:
            return False
    elif root2.right == None:
        return False
    else:
        if not identicalTrees( root1.right, root2.right ):
            return False

    return True
