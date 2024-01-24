import java.util.*;

public class Solution
{
    public static int occursOnce( int[] a, int n )
    {
        HashSet<Integer> set = new HashSet<>();

        for ( int i : a )
        {
            if ( set.contains( i ) )
            {
                set.remove( i );
            }
            else
            {
                set.add( i );
            }
        }

        return ( int ) set.toArray()[0];
    }
}
