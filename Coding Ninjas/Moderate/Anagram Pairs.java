import java.util.HashMap;

public class Solution
{

    public static boolean isAnagram( String str1, String str2 )
    {
        HashMap< Character, Integer > s1 = new HashMap<>();
        HashMap< Character, Integer > s2 = new HashMap<>();

        for ( char ch : str1.toCharArray() )
        {
            s1.put( ch, s1.getOrDefault( ch, 0 ) );
        }

        for ( char ch : str2.toCharArray() )
        {
            s2.put( ch, s2.getOrDefault( ch, 0 ) );
        }

        return s1.equals( s2 );
    }

}
