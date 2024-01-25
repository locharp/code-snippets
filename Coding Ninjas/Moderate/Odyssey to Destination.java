import java.util.*;

public class Solution
{

    static int minimumFlights( int n, int k, ArrayList<Integer> a )
    {
        List<Integer> c = a.subList( 1, a.size() - 1 );
        Collections.sort( c );
        
        for ( int i = 0; i < c.size(); i++ )
        {
            if ( c.get( i ) <= k )
            {
                n--;
                k -= c.get( i );
            }
            else
            {
                break;
            }
        }

        return --n;
    }

}
