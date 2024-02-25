public class Solution
{

    static int f
    ( int[][] mat, boolean[][]visited, int sx, int sy, int dx, int dy, int step )
    {
        if ( sx == dx && sy == dy )
        {
            return step;
        }
        else if ( sx < 0 || sx >= mat.length
            || sy < 0 || sy >= mat[0].length
            || mat[sx][sy] < 1 || visited[sx][sy] )
        {
            return -1;
        }

        visited[sx][sy] = true;
        int ans = -1;
        step++;
        ans = Math.max( f( mat, visited, sx - 1, sy, dx, dy, step ), ans );
        ans = Math.max( f( mat, visited, sx + 1, sy, dx, dy, step ), ans );
        ans = Math.max( f( mat, visited, sx, sy - 1, dx, dy, step ), ans );
        ans = Math.max( f( mat, visited, sx, sy + 1, dx, dy, step ), ans );
        visited[sx][sy] = false;
        
        return ans;
    }



    public static int longestPath
    ( int n, int m, int[][] mat, int sx, int sy, int dx, int dy )
    {
        boolean[][] visited = new boolean[n][m];
        
        return f( mat, visited, sx, sy, dx, dy, 0 );
    }

}
