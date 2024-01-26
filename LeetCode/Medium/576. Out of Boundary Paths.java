class Solution
{

    int[][][] dp;
    int MOD, m, n;



    int f( int i, int j, int k )
    {
        if ( i < 0 || i > m || j < 0 || j > n )
        {
            return 1;
        }
        else if ( k-- < 1 )
        {
            return 0;
        }
        else if ( dp[i][j][k] != -1 )
        {
            return dp[i][j][k];
        }

        int ans = 0;
        
        ans += f( i + 1, j, k );
        ans += f( i - 1, j, k );
        ans += f( i, j + 1, k );
        ans += f( i, j - 1, k );
        dp[i][j][k] = ans;

        return ans;
    }
    
    
    
    public int findPaths( int m, int n, int maxMove, int startRow, int startColumn )
    {

        dp = new int[m][n][maxMove];
        MOD = 1000000007;
        this.m = m - 1;
        this.n = n - 1;

        for ( int[][]r : dp )
        {
            for ( int[]s : r )
            {
                Arrays.fill( s, -1 );
            }
        }

        return f( startRow, startColumn, maxMove );
    }

}
