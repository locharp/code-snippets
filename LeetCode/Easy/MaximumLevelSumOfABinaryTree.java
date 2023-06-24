import java.util.Collections;
import java.util.Vector;

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
    void getLevelsValues( TreeNode root, Vector<Vector<Integer>> values, int level )
    {
        if ( values.size() < level )
        {
            values.addElement( new Vector<Integer>() );
        }
        
        values.elementAt( level - 1 ).addElement( root.val );
        
        if ( root.left != null )
        {
            getLevelsValues( root.left, values, level + 1 );
        }
        
        if ( root.right != null )
        {
            getLevelsValues( root.right, values, level + 1 );
        }
    }
    
    public int maxLevelSum(TreeNode root) {
        Vector<Vector<Integer>> values = new Vector<Vector<Integer>>();
        
        getLevelsValues( root, values, 1 );
        
        Vector<Integer> levelSums = new Vector<Integer>();
        
        for ( Vector<Integer> level : values )
        {
            levelSums.addElement( level.stream().mapToInt( Integer::valueOf ) .sum() );
        }
        
        int max = Collections.max ( levelSums );
        
        return levelSums.indexOf( max ) + 1;
    }
}