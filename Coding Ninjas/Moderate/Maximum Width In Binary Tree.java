import java.util.*;

public class Solution
{
    public static int getMaxWidth
    ( TreeNode root )
    {
        if ( root == null )
        {
            return 0;
        }
        
        ArrayDeque< TreeNode > q =
            new ArrayDeque<>();
        q.push( root );
        int ans = 0;

        while ( !q.isEmpty() )
        {
            ans = Math.max( q.size(), ans );
            
            for ( int i = q.size(); i > 0; i-- )
            {
                TreeNode node = q.poll();
                
                if ( node.left != null )
                {
                    q.offer( node.left );
                }

                if ( node.right != null )
                {
                    q.offer( node.right );
                }
            }
        }

        return ans;
    }

}
