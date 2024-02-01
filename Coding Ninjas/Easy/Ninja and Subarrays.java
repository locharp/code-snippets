public class Solution
{

    public static int sumOfSmallestAndSecondSmallest
    ( int n, int[] arr )
    {
        int ans = 0;

        for ( int i = 1; i < n; i++ )
        {
            ans = Math.max( arr[i] + arr[ i - 1 ], ans );
        }

        return ans;
    }

}
