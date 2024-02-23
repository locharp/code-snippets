import java.util.ArrayList;

public class Solution
{

    static void preorderTraversal
    ( BinaryTreeNode< Integer > root, ArrayList< Integer > ans )
    {
        if ( root == null )
        {
            return;
        }

        ans.add( root.data );
        preorderTraversal( root.left, ans );
        preorderTraversal( root.right, ans );
    }



	public static ArrayList< Integer > preorderTraversal
    ( BinaryTreeNode< Integer > root )
    {
		ArrayList< Integer > ans = new ArrayList<>();
        preorderTraversal( root, ans );

        return ans;
	}
    
}
