public class Solution
{
    public static String decode( String S )
    {
        S = new StringBuilder( S ).reverse().toString();
        int n = S.length();
        int m = n - 2;
        StringBuilder ans = new StringBuilder();

        for ( int i = 0; i < n; )
        {
            if ( i < m && Integer.parseInt( S.substring( i, i + 3 ) ) < 123 )
            {
                ans.append( ( char ) Integer.parseInt( S.substring( i, i + 3 ) ) );
                i += 3;
            }
            else
            {
                ans.append( ( char ) Integer.parseInt( S.substring( i, i + 2 ) ) );
                i += 2;
            }
        }

        return ans.toString();
    }
}
