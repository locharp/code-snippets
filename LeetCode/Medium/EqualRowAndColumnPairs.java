class EqualRowAndColumnPairs
{
    public int equalPairs( int[][] grid )
    {
        int count = 0;
        int len = grid.length;
        
        for ( int h = 0; h < len; h++ )
        {
            for ( int i = 0; i < len; i++ )
            {
                for ( int j = 0; j < len; j++ )
                {
                    if ( grid[h][j] != grid[j][i] )
                    {
                        count--;
                        break;
                    }
                }
            
            count++;
            }
        }
        
        return count;
    }
}