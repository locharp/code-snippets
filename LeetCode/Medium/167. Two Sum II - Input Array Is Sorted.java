class Solution
{
    
    int f( int[] nums, int i, int j, int t )
    {
        while ( i < j )
        {
            int k = ( i + j ) / 2;
            
            if ( nums[k] >= t )
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
    
    
    
    
    public int[] twoSum( int[] numbers, int target )
    {
        int d = ( target + 1 ) / 2;
        int n = numbers.length - 1;
        int m = f( numbers, 0, n, d );
        
        if ( numbers[m] == d && m < n && numbers[ m + 1 ] == target - d )
        {
            return new int[] { m + 1, m + 2 };
        }
        
        d = target - numbers[0];
        int j = f( numbers, m, n, d );
        
        if ( numbers[j] == d )
        {
            return new int[] { 1, j + 1 };
        }
        
        for ( int i = 1; i < m; i++ )
        {
            if ( numbers[i] == numbers[ i - 1 ] )
            {
                continue;
            }
            
            d = target - numbers[i];
            j = f( numbers, m, n, d );
            
            if ( numbers[j] == d )
            {
                return new int[] { i + 1, j + 1 };
            }
        }
        
        return new int[] { 1, 2 };
    }
    
}
