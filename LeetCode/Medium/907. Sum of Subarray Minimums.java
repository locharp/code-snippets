class Solution
{
    public int sumSubarrayMins( int[] arr )
    {
        Long MOD = 1000000007L;
        Long ans = 0L;
        Long j = 0L;
        Long k = 0L;
        Long m = 0L;
        Long n = 0L;
        Long o = Long.valueOf( arr.length );
        ArrayDeque<Long> q = new ArrayDeque<>();
        
        for ( Long i = 0L; i < o; i++ )
        {
            while ( !q.isEmpty() && arr[ q.peekLast().intValue() ] > arr[ i.intValue() ] )
            {
                j = q.pollLast();
                
                if ( q.isEmpty() )
                {
                    k = -1L;
                }
                else
                {
                    k = q.peekLast();
                }
                
                m = j - k;
                n = i - j;
                ans = ( ans + ( arr[ j.intValue() ] * m * n ) ) % MOD;
            }
            
            q.offerLast( i );
        }
        
        while ( !q.isEmpty() )
        {
            j = q.pollLast();
            
            if( q.isEmpty() )
            {
                k = -1L;
            }
            else
            {
                k = q.peekLast();
            }
            
            m = j - k;
            n = o - j;
            ans = ( ans + ( arr[ j.intValue() ] * m * n ) ) % MOD;
        }
        
        return ans.intValue();
    }
}
