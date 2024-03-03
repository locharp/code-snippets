class Solution
{
    
    public int countSubmatrices
    ( int[][] grid, int k )
    {
        int ans = 0;
        int[] a = new int[ grid[0].length ];
        
        
        for ( int i = 0; i < grid.length; i++ )
        {
            a[0] += grid[i][0];
            
            if ( a[0] <= k )
            {
                ans++;
            }
            else
            {
                break;
            }
            
            
            for ( int j = 1; j < grid[0].length; j++ )
            {
                grid[i][j] += grid[i][ j - 1 ];
                a[j] += grid[i][j];
                
                if ( a[j] <= k )
                {
                    ans++;
                }
                else
                {
                    break;
                }
            }
        }
        
        
        return ans;
    }
    
}
