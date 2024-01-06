public class Solution
{
    public static String shortenToDate( String longDate )
    {
        int i = longDate.indexOf( ',' );
        
        return longDate.substring( 0, i );
    }
}
