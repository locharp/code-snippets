public class Solution
{

    public static int longestSubarrayWithSumK
    ( int []a, long k )
    {
        int ans = 0;
        int sum = 0;
        int i = 0;
        int j = 0;

        for ( ; j < a.length; j++ )
        {
            sum += a[j];

            while ( sum > k )
            {
                sum -= a[ i++ ];
            }

            if ( sum == k )
            {
                ans = Math.max( j - i + 1, ans );
            }
        }

        return ans;
    }

}
