public class Solution
{

    public static boolean isPeriodic( String s )
    {
        for ( int i = 2; i <= s.length(); i++ )
        {
            if ( s.length() % i != 0 )
            {
                continue;
            }

            if ( s.substring( 0, s.length() / i ).repeat( i ).equals( s ) )
            {
                return true;
            }
        }
        
        return false;
    }
}
