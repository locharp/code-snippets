import java.util.*;

public class Solution
{

    static int canYouMakeEqual
    ( int n, ArrayList< Integer > v )
    {
        HashSet< Integer > set = new HashSet<>();
        set.addAll( v );
        v.clear();
        v.addAll( set );
        Collections.sort( v );

        for ( int i = 1; i < v.size(); i++ )
        {
            int j = v.get( i - 1 );

            while ( j < v.get( i ) )
            {
                j += j;
            }

            if ( j > v.get( i ) )
            {
                return 0;
            }
        }

        return 1;
    }

}
