import java.util.ArrayList;

public class Solution
{

    static int findTheLarger
    ( int n, ArrayList< Integer > v )
    {
        int ans = 0;
        int i = 0;
        int s = 0;
        int t = 0;
        int m = n - 1;
        

        for ( ; i < m; i++ )
        {
            s += v.get( i );
            
            if ( v.get( i ) > v.get( i + 1 ) )
            {
                break;
            }
        }
        

        if ( i == m )
        {
            s += v.get( i );
        }

        for ( ; i < n; i++ )
        {
            t += v.get( i );
        }
        

        if ( s > t )
        {
            return 0;
        }
        else if ( s < t )
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }

}
