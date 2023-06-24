class TwoSum
{
    public int[] twoSum( int[] nums, int target )
    {
        final int len = nums.length;
    
        for ( int i = 0; i < len; i++ )
        {
            final int diff = target - nums[i];
            
            for ( int j = i + 1 ; j < len ; j++ )
            {
                if ( diff == nums[j] )
                {
                    return new int[] { i, j };
                }
            }
        }
    
        return new int[2];
    }
}