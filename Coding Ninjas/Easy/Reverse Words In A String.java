public class Solution 
{
    
    public static String reverseString
    ( String str ) 
    {
        String[] s = str.split( " " );
        StringBuilder ans = new StringBuilder();
        ans.append( s[ s.length - 1 ] );

        for ( int i = s.length - 2; i >= 0; i-- )
        {
            ans.append( " " + s[i] );
        }
        
        return ans.toString();
    }
    
}
