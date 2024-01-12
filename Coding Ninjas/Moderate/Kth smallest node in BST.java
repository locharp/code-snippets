import java.util.ArrayList;

public class Solution
{
    static void f( ArrayList<Integer> arr, TreeNode root )
    {
        if ( root == null )
        {
            return;
        }

        f( arr, root.left );
        arr.add( root.data );
        f( arr, root.right );
    }



    public static int kthSmallest( TreeNode root, int k )
    {
        ArrayList<Integer> arr = new ArrayList<>();
        f( arr, root );

        return arr.get( k - 1 );
    }
}
