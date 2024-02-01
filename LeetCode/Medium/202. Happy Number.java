class Solution
{
    
    public boolean isHappy
    ( int n )
    {
        HashSet< Integer > set =
            new HashSet<>();
        
        while ( n > 1 && !set.contains( n ) )
        {
            set.add( n );
            int o = 0;
            
            while ( n > 0 )
            {
                o += square( n % 10 );
                n /= 10;
            }
            
            n = o;
        }
        
        return n == 1;
    }
    
    
    
    int square
    ( int n )
    {
        return n * n;
    }
    
}
