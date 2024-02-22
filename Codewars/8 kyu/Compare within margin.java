public class Solution
{
    
    public static int closeCompare
    ( double a, double b )
    {
        return closeCompare( a, b, 0 );
    }
    
    
    
    public static int closeCompare
    ( double a, double b, double margin )
    {
        double d = a - b;
        
        if ( Math.abs( d ) <= margin )
        {
            return 0;
        }
        else
        {
            if ( d > 0 )
            {
                return 1;
            }
            else
            {
                return -1;
            }
        }
    }
    
}
