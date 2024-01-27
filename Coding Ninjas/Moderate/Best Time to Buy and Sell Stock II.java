public class Solution
{

    public static long getMaximumProfit ( int n, long[] values )
    {
        if ( values.length < 2 )
        {
            return 0;
        }

        long ans = 0;
        long c = values[0];

        for ( long i : values )
        {
            if ( i > c )
            {
                ans += i - c;
                c = i;
            }
            else
            {
                c = i;
            }
        }

        return ans;
    }

}
