public class Solution
{

    public static String revWords
    ( String str )
    {
        String[] s = str.split( "\\s+" );
        int n = s.length - 1;
        String[] ans = new String[ n + 1 ];
        
        for ( int i = 0; i <= n; i++ )
        {
            ans[ n - i ] = s[i];
        }

        return String.join( " ", ans );
    }

}
