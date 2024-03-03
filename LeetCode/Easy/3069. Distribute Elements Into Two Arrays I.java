class Solution
{
    
    public int[] resultArray
    ( int[] nums )
    {
        int[] nums2 = new int[nums.length];
        nums2[0] = nums[1];
        int p = 0;
        int q = 0;
        
        for ( int h = 2; h < nums.length; h++ )
        {
            if ( nums[p] > nums2[q] )
            {
                nums[ ++p ] = nums[h];
            }
            else
            {
                nums2[ ++q ] = nums[h];
            }
        }
        
        System.arraycopy( nums2, 0, nums, ++p, ++q );
        
        return nums;
    }
    
}
