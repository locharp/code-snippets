public class ANeedleInTheHaystack
{
    public static String findNeedle(Object[] haystack)
    {
        // Your code here
        int needle = -1;
    
        for ( int i = 0; i < haystack.length; i++ )
        {
            if ( haystack[i] == "needle" )
            {
                needle = i;
                break;
            }
        }
        
        return "found the needle at position " + needle;
    }
}