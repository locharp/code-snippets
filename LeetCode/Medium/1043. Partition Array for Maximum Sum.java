class Solution
{
    
    public int maxSumAfterPartitioning
    ( int[] arr, int k )
    {
        int dp = new int[ arr.length ];
        Arrays.fill( dp, -1 );
        
        return maxSum( arr, k, dp, 0 );
    }
    
    
    
    int maxSum
    ( int[] arr, int k, int[] dp, int i )
    {
        if ( i >= arr.length )
        {
            return 0;
        }
        else if ( dp[i] >= 0 )
        {
            return dp[i];
        }
        
        int m = 0;
        int n = Math.min( i + k, arr.length );
        
        for ( int j = i; j < n; j++ )
        {
            m = Math.max( arr[j], m );
            int sum = m * ( j - 1 + 1 );
            sum += maxSum( arr, k, dp, j + 1 );
            dp[i] = Math.max( sum, dp[i] );
        }
        
        return dp[i];
    }
    
}
