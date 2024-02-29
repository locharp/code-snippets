import java.util.*;

public class Solution
{

    public static ArrayList< Integer > findAnagramsIndices
    ( String str, int n, String ptr, int m )
    {
        HashMap< Character, Integer > p = new HashMap<>();
        HashMap< Character, Integer > q = new HashMap<>();
        ArrayList< Integer > ans = new ArrayList<>();
        m--;

        for ( char ch : ptr.toCharArray() )
        {
            p.put( ch, p.getOrDefault( ch, 0 ) + 1 );
        }

        for ( int i = 0; i < m; i++ )
        {
            q.put( str.charAt( i ), q.getOrDefault( str.charAt( i ), 0 ) + 1 );
        }

        for ( int i = m, j = 0; i < n; i++, j++ )
        {
            q.put( str.charAt( i ), q.getOrDefault( str.charAt( i ), 0 ) + 1 ) ;

            if ( p.equals( q ) )
            {
                ans.add( j );
            }

            if ( q.get( str.charAt( j ) ) < 2 )
            {
                q.remove( str.charAt( j ) );
            }
            else
            {
                q.put( str.charAt( j ), q.get( str.charAt( j ) ) - 1 );
            }
        }

        return ans;
    }

}
