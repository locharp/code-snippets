
public class Solution
{
    
    static void f( boolean[] p )
    {
        for ( int i = 4; i < p.length; i += 2 )
        {
            p[i] = true;
        }
        
        for ( int i = 3; i <= p.length / 2; i += 2 )
        {
            if ( p[i] )
            {
                continue;
            }
            
            for ( int j = i * 2; j < p.length; j += i )
            {
                p[j] = true;
            }
        }
    }
    
    
    
    static int gcd( int x, int y )
    {
        if ( y == 0 )
        {
            return x;
        }
        else
        {
            return gcd( y, x % y );
        }
    }
    
    
    
    public static long gcdSum( int n )
    {
        boolean[] p = new boolean[ n + 1 ];
        f( p );
        long ans = 0;
        
        for ( int i = 1; i < n; i++ )
        {
            if ( !p[i] )
            {
                int k = n / i - 1;
                ans += k * i + n - k - i;
                continue;
            }
            
            for ( int j = i + 1; j <= n; j++ )
            {
                if ( p[j] )
                {
                    ans += gcd( i, j );
                }
                else
                {
                    ans++;
                }
            }
        }
        
        return ans;
    }
}
}
