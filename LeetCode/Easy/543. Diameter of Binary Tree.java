class Solution
{

    int ans;



    Solution
    ()
    {
        ans = 0;
    }


    
    int f
    ( TreeNode root )
    {
        if ( root == null )
        {
            return 0;
        }

        int left = f( root.left );
        int right = f( root.right );
        ans = Math.max( left + right, ans );

        return Math.max( left, right ) + 1;
    }

    public int diameterOfBinaryTree
    ( TreeNode root )
    {
        f( root );

        return ans;
    }

}
