public class Solution
{
    public int Search( int[] nums, int target )
    {
        int i = 0;
        int j = nums.Length - 1;
        int n = j;

        while ( nums[i] > nums[j] )
        {
            int k = i + ( ( j - i ) / 2 );

            if ( nums[i] <= nums[k] )
            {
                i = k + 1;
            }
            else
            {
                j = k;
            }
        }
        
        if ( target > nums[n] )
        {
            i = 0;
        }
        else
        {
            j = n;
        }
        
        while ( i < j )
        {
            int k = i + ( ( j - i ) / 2 );
            
            if ( nums[k] < target )
            {
                i = k + 1;
            }
            else
            {
                j = k;
            }
        }
        
        if ( nums[i] == target )
        {
            return i;
        }
        else
        {
            return -1;
        }
    }
}
