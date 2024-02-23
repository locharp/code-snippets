public class Solution
{
    
    public static int maxDepth( String s )
    {
        int ans = 0;
        int curr = 0;

        for ( char ch : s.toCharArray() )
        {
            if ( ch == '(' )
            {
                curr++;
                ans = Math.max( curr, ans );
            }
            else if ( ch == ')' )
            {
                curr--;
            }
        }

        return ans;
    }
    
}
