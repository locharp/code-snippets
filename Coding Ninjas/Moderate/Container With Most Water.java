public class Solution
{
    
    public static int maxArea
    ( int[] height )
    {
        int i = 0;
        int j = height.length - 1;
        int ans = 0;
        
        while ( i < j )
        {
            ans = Math.max( Math.min( height[i], height[j] ) * ( j - i ), ans );

            if ( height[i] > height[j] )
            {
                j--;
            }
            else
            {
                i++;
            }
        }

        return ans;
    }

}
