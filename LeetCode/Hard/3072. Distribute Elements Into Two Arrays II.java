class Solution
{
    
    int f( ArrayList< Integer > arr, int j, Integer t )
    {
        int i = 0;
        
        while ( i < j )
        {
            int k = ( i + j ) / 2;
            
            if ( arr.get( k ) <= t )
            {
                i = k + 1;
            }
            else
            {
                j = k;
            }
        }
        
        return i;
    }
    
    
    
    public int[] resultArray
    ( int[] nums )
    {
        ArrayList< Integer > arr1 = new ArrayList<>();
        ArrayList< Integer > arr2 = new ArrayList<>();
        arr1.add( nums[0] );
        arr2.add( nums[1] );
        int[] nums2 = new int[nums.length];
        nums2[0] = nums[1];
        int p = 1;
        int q = 1;
        
        for ( int h = 2; h < nums.length; h++ )
        {
            int i = f( arr1, p, nums[h] );
            int j = f( arr2, q, nums[h] );
            int m = arr1.size() - i;
            int n = arr2.size() - j;
            
            if ( m > n )
            {
                arr1.add( i, nums[h] );
                nums[p++] = nums[h];
            }
            else if ( m < n || arr1.size() > arr2.size() )
            {
                arr2.add( j, nums[h] );
                nums2[q++] = nums[h];
            }
            else
            {
                arr1.add( i, nums[h] );
                nums[p++] = nums[h];
            }
        }
        
        System.arraycopy( nums2, 0, nums, p, q );
        
        return nums;
    }
    
}
