import java.util.*;

public class Solution
{

    static int boredChef
    ( int n, int k, String s )
    {
        HashMap< Character, Integer > map = new HashMap<>();

        for ( char ch : s.toCharArray() )
        {
            map.put( ch, map.getOrDefault( ch, 0 ) + 1 );
        }

        if ( Collections.max( map.values() ) >= k )
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

}
