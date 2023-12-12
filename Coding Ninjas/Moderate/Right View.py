# Following is the Binary Tree node structure:
class BinaryTreeNode:

    def __init__ ( self,data ):

        self.data=data
        self.left=None
        self.right=None

        


        
def f( ans, root, i ):

    if root == None:
        return
    elif len( ans ) <= i:
        ans.append( root.data )

    f( ans, root.right, i + 1 )
    f( ans, root.left, i + 1 )



def printRightView( root ):

    ans = []
    f( ans, root, 0 )

    return ans
