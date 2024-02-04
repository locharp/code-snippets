public class Solution
{
    public static long countOf3
    ( int x )
    {
        String s = Integer.toString( x );
        int m = s.length() - 1;
        int[] a = new int[ m + 1 ];
        long ans = 0;

        for ( int i = 0; i < m; i++ )
        {
            a[ i + 1 ] = a[i] * 10 + ( int ) Math.pow( 10, i );
        }  
        
        for ( int i = 0; i <= m; i++ )
        {
            if ( s.charAt( i ) > '3' )
            {
                ans += ( int ) Math.pow( 10, m - i );
            }
            else if ( s.charAt( i ) == '3' )
            {
                ans += ( x % ( int ) Math.pow( 10, m - i ) ) + 1;
            }
            
            ans += a[ m - i ] * Character.getNumericValue( s.charAt( i ) );
        }

        return ans;
    }

}
