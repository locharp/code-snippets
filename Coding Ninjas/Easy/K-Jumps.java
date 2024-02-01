import java.util.*;

public class Solution
{

    static long kJumps
    ( int n, int k, ArrayList<Integer> a )
    {
        long ans = 0;

        for ( int i = 0; i < k; i++ )
        {
            long sum = 0;

            for ( int j = i; j < n; j += k )
            {
                sum += a.get( j );
            }

            ans = Math.max( sum, ans );
        }

        return ans;
    }

}
