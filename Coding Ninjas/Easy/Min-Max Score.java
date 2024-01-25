import java.util.*;

public class Solution
{

    static int maximumScore( int n, ArrayList<Integer> v )
    {
        Collections.sort( v );

        return v.get( 0 ) + v.get( v.size() / 2 );
    }

}
