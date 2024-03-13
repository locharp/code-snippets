class Solution
{
    
    int f
    ( int n, int p )
    {
        int m = n * ( n + 1 ) / 2;
        int q = p * ( p + 1 ) / 2;
        
        
        return ( q - p ) - ( m - q );
    }
    
    
    
    public int pivotInteger
    ( int n )
    {
        int i = 1;
        int j = n;
        
        
        while ( i <= j )
        {
            int k = ( i + j ) / 2;
            int o = f( n, k );
            
            if ( o > 0 )
            {
                j = k - 1;
            }
            else if ( o < 0 )
            {
                i = k + 1;
            }
            else
            {
                return k;
            }
        }
        
        
        return -1;
    }
    
}
