class Solution
{
    public int findPeakElement( int[] nums )
    {
        int i = 0;
        int j = nums.length - 1;
        int k;
        
        while( i < j )
        {
            k = ( i + j ) / 2;
            
            if ( nums[k] > nums[ k + 1 ] )
            {
                j = k;
            }
            else
            {
                i = k + 1;
            }
        }
        
        return i;
    }
}
