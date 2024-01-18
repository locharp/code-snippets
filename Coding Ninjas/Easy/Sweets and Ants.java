public class Solution
{

    public static int[] sweet( int[] S )
    {
        int n = S.length;
        int[] ans = new int[n];
        int s = 0;

        for ( int i = n - 1; i >= 0; i-- )
        {
            s = Math.max( S[i], s );
            ans[i] = Math.min( s--, 1 );
        }

        return ans;
    }
}
