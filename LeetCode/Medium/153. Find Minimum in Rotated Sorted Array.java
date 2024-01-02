class Solution
{
    public int findMin( int[] nums )
    {
        int i = 0;
        int j = nums.length - 1;
        int k = 0;
        
        while ( i < j )
        {
            k = ( i + j ) / 2;
            
            if ( nums[0] > nums[k] )
            {
                j = k;
            }
            else
            {
                i = k + 1;
            }
        }
        
        if ( i == nums.length - 1 )
        {
            return Math.min( nums[0], nums[i] );
        }
        else
        {
            return nums[i];
        }
    }
}
