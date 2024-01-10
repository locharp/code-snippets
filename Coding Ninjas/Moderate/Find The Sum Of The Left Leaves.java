public class Solution
{

	public static int sumOfLeftLeaves( TreeNode<Integer> root )
	{
		return sumOfLeftLeaves( root, false );
	}

	

    static int sumOfLeftLeaves( TreeNode<Integer> root, boolean t )
	{
        if ( root == null )
		{
			return 0;
		}

		int ans = 0;

		if ( root.left == null && root.right == null && t )
		{
			ans += root.data;
		}

		ans += sumOfLeftLeaves( root.left, true );
		ans += sumOfLeftLeaves( root.right, false );

		return ans;
    }
}
