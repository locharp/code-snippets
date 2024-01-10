class Solution
{
    public int missingInteger( int[] nums )
    {
        int ans = nums[0];
        
        for ( int i = 1; i < nums.length; i++ )
        {
            if ( nums[i] == nums[ i - 1 ] + 1 )
            {
                ans += nums[i];
            }
            else
            {
                break;
            }
        }
        
        Arrays.sort( nums );
        
        for ( int num : nums )
        {
            if ( ans == num )
            {
                ans += 1;
            }
            else if ( ans < num )
            {
                break;
            }
        }
        
        return ans;
    }
}
