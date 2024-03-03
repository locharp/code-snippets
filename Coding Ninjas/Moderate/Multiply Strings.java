public class Solution
{

    public static String multiplyStrings
    ( String a, String b )
    {
        int n = a.length();
        int m = b.length();
        int o = m + n;
        int[] p = new int[n];
        int[] q = new int[m];
        int[] arr = new int[ o ];
        StringBuilder ans = new StringBuilder();

        
        for ( int i = 0; i < n; i++ )
        {
            p[i] = Character.getNumericValue( a.charAt( i ) );
        }
        

        for ( int i = 0; i < m; i++ )
        {
            q[i] = Character.getNumericValue( b.charAt( i ) );
        }


        for ( int i = 1; i <= n; i++ )
        {
            for ( int j = 1; j <= m; j++ )
            {
                arr[ i + j - 2 ] += p[ n - i ] * q[ m - j ];
            }
        }

        
        for ( int c = 0, i = 0; i < o; i++ )
        {
            c += arr[i];
            ans.append( c % 10 );
            c /= 10;
        }


        int j = ans.length() - 1;


        while ( j > 0 && ans.charAt( j ) < '1' )
        {
            j--;
        }


        ans.setLength( j + 1 );


        return ans.reverse().toString();
    }

}
