public class Solution
{

    public static int[] generateFibonacciNumbers
    ( int n )
    {
        int[] ans = new int[n];
        
        if ( n < 2 )
        {
            return ans;
        }

        ans[1] = 1;

        for ( int i = 2; i < n; i++ )
        {
            ans[i] = ans[ i - 1 ] + ans[ i - 2 ];
        }

        return ans;
    }
}
