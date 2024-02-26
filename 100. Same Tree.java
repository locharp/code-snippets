class Solution
{

    public boolean isSameTree
    ( TreeNode p, TreeNode q )
    {
        if ( p == null )
        {
            if ( q == null )
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else if ( q == null || p.val != q.val )
        {
            return false;
        }
      

        if ( p.left == null )
        {
            if ( q.left != null )
            {
                return false;
            }
        }
        else if ( q.left == null || !isSameTree( p.left, q.left ) )
        {
            return false;
        }
      
        
        if ( p.right == null )
        {
            if ( q.right != null )
            {
                return false;
            }
        }
        else if ( q.right == null || !isSameTree( p.right, q.right ) )
        {
            return false;
        }

        return true;
    }

}
