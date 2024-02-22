import java.util.*;

public class Solution
{
    static int canYouMakeDifference
    ( int n, String s )
    {
        HashSet< Character > set =
            new HashSet<>();

        for ( char ch : s.toCharArray() )
        {
            set.add( ch );
        }

        if ( set.size() != 1 )
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

}
