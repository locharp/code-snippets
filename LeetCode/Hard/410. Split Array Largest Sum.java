class Solution
{
    
    public int splitArray( int[] nums, int k )
    {
        IntStream s = IntStream.of( nums );
        int i = s.max().getAsInt();
        int j = IntStream.of( nums ).sum();
        
        while ( i < j )
        {
            int m = ( i + j ) / 2;
            int c = 1;
            int d = 0;
            
            for ( int n : nums )
            {
                if ( d + n <= m )
                {
                    d += n;
                }
                else
                {
                    d = n;
                    c++;
                }
            }
            
            if ( c > k )
            {
                i = m + 1;
            }
            else
            {
                j = m;
            }
        }
        
        return j;
    }
    
}
