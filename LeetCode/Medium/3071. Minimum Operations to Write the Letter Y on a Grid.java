class Solution
{
    
    public int minimumOperationsToWriteY
    ( int[][] grid )
    {
        int ans = Integer.MAX_VALUE;
        int n = grid.length;
        int o = n / 2;
        int m = n + o;
        int p = n * n - m;
        int[] x = new int[3];
        int[] y = new int[3];
        
        
        for ( int i = 0; i < n; i++ )
        {
            for ( int j = 0; j < n; j++ )
            {
                if ( i < o && ( i == j || n - i - 1 == j )
                    || j == o && i >= o )
                {
                    y[ grid[i][j] ]++;
                }
                else
                {
                    x[ grid[i][j] ]++;
                }
            }
        }
        
        
        for ( int i = 0; i < 3; i++ )
        {
            x[i] = m - x[i];
            y[i] = p - y[i];
        }
        
        
        for ( int i = 0; i < 3; i++ )
        {
            for ( int j = 0; j < 3; j++ )
            {
                if ( i == j )
                {
                    continue;
                }
                
                ans = Math.min( x[i] + y[j], ans );
            }
        }
        
        
        return ans;
    }
    
}
