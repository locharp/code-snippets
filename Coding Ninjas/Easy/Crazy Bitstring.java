import java.util.*;

public class Solution
{

    static long crazyBitstring( int n, String s, ArrayList<Integer> a )
    {
        ArrayList<Integer> d = new ArrayList<>();
        ArrayList<Integer> e = new ArrayList<>();

        for ( int i = 0; i < n; i++ )
        {
            if ( s.charAt( i ) == '0' )
            {
                d.add( a.get( i ) );
            }
            else
            {
                e.add( a.get( i ) );
            }
        }

        Collections.sort( d );
        Collections.sort( e );

        if ( d.size() < e.size() )
        {
            ArrayList<Integer> f = d;
            d = e;
            e = f;
        }

        int c = d.size() - e.size();
        long g = 0;
        long h = 0;

        for ( int i = 0; i < c; i++ )
        {
            g += d.get( i );
        }

        for ( Integer i : e )
        {
            h += i;
        }

        return Math.min( g, h );
    }

}
    }

}
