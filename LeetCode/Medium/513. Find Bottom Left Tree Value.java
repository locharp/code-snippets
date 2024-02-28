/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution
{

    int ans;
    int depth;



    Solution
    ()
    {
        ans = -1;
        depth = -1;
    }



    void f
    ( TreeNode root, int d )
    {
        if ( root == null )
        {
            return;
        }
        else if ( d > depth )
        {
            ans = root.val;
            depth = d;
        }

        f( root.left, d + 1 );
        f( root.right, d + 1 );
    }



    public int findBottomLeftValue
    ( TreeNode root )
    {
        f( root, 0 );

        return ans;
    }

}
