import java.util.Arrays;
class Solution
{

    public static int assignCookie
    ( int []greed, int []size )
    {
        int ans = 0;
        Arrays.sort( greed );        
        Arrays.sort( size );

        for ( int i = greed.length - 1, j = size.length - 1;
            i >= 0 && j >= 0;
            i-- )
        {
            if ( greed[i] <= size[j] )
            {
                ans++;
                j--;
            }
        }

        return ans;
    }

}
