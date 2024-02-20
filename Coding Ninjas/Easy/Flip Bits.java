public class Solution
{

    public static int flipBits
    ( int A, int B )
    {
        int ans = 0;
        String s = String.format( "%32s", Integer.toBinaryString( A ) ).replace( ' ', '0' );
        String t = String.format( "%32s", Integer.toBinaryString( B ) ).replace( ' ', '0' );
        
        for ( int i = 0; i < s.length(); i++ )
        {
            if ( s.charAt( i ) != t.charAt( i ) )
            {
                ans++;
            }
        }

        return ans;
    }
    
}
