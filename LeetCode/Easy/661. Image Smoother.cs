public class Solution
{
    public int[][] ImageSmoother( int[][] img )
    {
        int m = img.Length;
        int n = img[0].Length;
        int[][] ans = new int[m][];

        for ( int i = 0; i < m; i++ )
        {
            ans[i] = new int[n];

            for ( int j = 0; j < n; j++ )
            {
                int p = Math.Max( 0, i - 1 );
                int q = Math.Min( m, i + 2 );
                int r = Math.Max( 0, j - 1 );
                int s = Math.Min( n, j + 2 );
                int t = 0;
                
                for ( int u = p; u < q; u++ )
                {
                    t += img[u][r..s].Sum();
                }

                ans[i][j] = t / ( ( q - p ) * ( s - r ) );
            }
        }
        
        return ans;
    }
}
