class Solution
{
    public int numRollsToTarget( int n, int k, int target )
    {
        int[] prev = new int[ target + 1 ];
        prev[0] = 1;
        long MOD = 1000000007;
        
        for ( int x = 0; x < n; x++ )
        {
            int[] curr = new int[ target + 1 ];
            
            for ( int y = 1; y <= target; y++ )
            {
                long temp = 0;
                
                for ( int z = Math.max( 0, y - k ); z < y; z++ )
                {
                   temp += prev[z];
                }
                
                curr[y] = ( int ) ( temp % MOD );
            }
            
            prev = curr;
        }
        
        return prev[target];
    }
}
