import java.util.*;

public class PangramChecker
{    

    public boolean check( String sentence )
    {
        HashSet< Character > ans =
            new HashSet<>();
        HashSet< Character > chars =
            new HashSet<>();
        sentence = sentence.toUpperCase();
        
        for ( char ch = 'A'; ch <= 'Z'; ch++ )
        {
            chars.add( ch );
        }
        
        for ( Character ch : sentence.toCharArray() )
        {
            if ( chars.contains( ch ) )
            {
                ans.add( ch );
            }
        }
        
        return ans.size() == 26;
    }
    
}
