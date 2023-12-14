class Solution
{
    public int[][] onesMinusZeros( int[][] grid )
    {
        int m = grid.length;
        int n = grid[0].length;
        int[][] diff = new int[m][n];
        int[] onesRow = new int[m];
        int[] onesCol = new int[n];

        for ( int i = 0; i < m; i++ )
        {
            for ( int j = 0; j < n; j++ )
            {
                if ( grid[i][j] == 1 )
                {
                    onesRow[i] += 1;
                    onesCol[j] += 1;
                }
            }
        }

        for ( int i = 0; i < m; i++ )
        {
            for ( int j = 0; j < n; j++ )
            {
                diff[i][j] = ( onesRow[i] - ( n - onesRow[i] ) ) + ( onesCol[j] - ( m - onesCol[j] ) );
            }
        }
        
        return diff;
    }
}
