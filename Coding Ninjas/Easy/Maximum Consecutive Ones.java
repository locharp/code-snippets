public class Solution
{
    
    public static int consecutiveOnes( int n, int[] arr )
    {
        int ans = 0;
        
        for ( int i = 0, c = 0; c + n - i > ans; i++ )
        {
            if ( arr[i] > 0 )
            {
                c++;
                ans = Math.max( c, ans );
            }
            else
            {
                c = 0;
            }
        }
        
        return ans;
    }
    
}
