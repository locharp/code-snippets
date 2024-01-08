class Solution
{
    int ans;

    Solution ()
    {
        this.ans = 0;
    }



    public int rangeSumBST( TreeNode root, int low, int high )
    {
        if ( root == null )
        {
            return this.ans;
        }

        if ( root.val > low )
        {
            this.rangeSumBST( root.left, low, high );
        }

        if( root.val < high )
        {
            this.rangeSumBST( root.right, low, high );
        }

        if( root.val >= low && root.val <= high )
        {
            this.ans += root.val;
        }
        
        return this.ans;
    }
}
