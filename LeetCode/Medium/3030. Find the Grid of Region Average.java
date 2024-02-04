class Solution
{

    public int[][] resultGrid
    ( int[][] image, int threshold )
    {
        int m = image.length;
        int n = image[0].length;
        int[][] ans = new int[m][n];
        Pixel[][] img =
            new Pixel[m][n];
        
        for ( int i = 0; i < m; i++ )
        {
            for ( int j = 0; j < n; j++ )
            {
                img[i][j] = new Pixel();
            }
        }
        
        for ( int i = 2; i < m; i++ )
        {
            for ( int j = 2; j < n; j++ )
            {
                int maxDiff = 0;
                int sum = 0;
                
                for ( int p = i - 2; p <= i; p++ )
                {
                    for ( int q = j - 2; q <= j; q++ )
                    {
                        if ( p < i )
                        {
                            maxDiff = Math.max( Math.abs( image[p][q] - image[ p + 1 ][q] ), maxDiff );
                        }
                        
                        if ( q < j )
                        {
                             maxDiff = Math.max( Math.abs( image[p][q] - image[p][ q + 1 ] ), maxDiff );
                        }
                        
                        sum += image[p][q];
                    }
                }
                
                if ( maxDiff <= threshold )
                {
                    int avg = sum / 9;
                    
                    for ( int p = i - 2; p <= i; p++ )
                    {
                        for ( int q = j - 2; q <= j; q++ )
                        {
                            img[p][q].addVal( avg );
                        }
                    }
                }
            }
        }
        
        for ( int i = 0; i < m; i++ )
        {
            for ( int j = 0; j < n; j++ )
            {
                if ( img[i][j].count > 0 )
                {
                    ans[i][j] = img[i][j].getVal();
                }
                else
                {
                    ans[i][j] = image[i][j];
                }
            }
        }
        
        return ans;
    }

}
                    




class Pixel
{
    
    int val;
    int count;
    
    
    
    void addVal( int val )
    {
        this.val += val;
        this.count++;
    }
    
    
    
    int getVal()
    {
        return val / count;
    }
    
}
