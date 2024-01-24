import java.util.*;
import java.util.stream.*;

public class Solution
{

    public static List<Integer> sortedArray( int []a, int []b )
    {
        int i = 0;
        int j = 0;
        int m = Integer.MIN_VALUE;
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add( m );

        while ( i < a.length && j < b.length )
        {
            if ( a[i] > b[j] )
            {
                if ( b[j] > m )
                {
                    m = b[j];
                    ans.add( m );
                }

                j++;
            }
            else
            {
                if ( a[i] > m )
                {
                    m = a[i];
                    ans.add( m );
                }

                i++;
            }
        }

        while ( i < a.length )
        {
            if ( a[i] > m )
            {
                m = a[i];
                ans.add( m );
            }

            i++;
        }

        while ( j < b.length )
        {
            if ( b[j] > m )
            {
                m = b[j];
                ans.add( m );
            }

            j++;
        }

        ans.remove( 0 );

        return ans;
    }
}
