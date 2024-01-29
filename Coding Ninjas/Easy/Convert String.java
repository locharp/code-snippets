public class Solution
{
    
    public static String convertString
    ( String str )
    {
        StringBuilder ans =
            new StringBuilder();
        boolean up =
            true;
        
        for ( char ch : str.toCharArray() )
        {
            if ( ch == ' ' )
            {
                up = true;
            }
            else if ( up )
            {
                ch = Character.toUpperCase( ch );
                up = false;
            }
            
            ans.append( ch );
        }
        
        return ans.toString();
    }
    
}
