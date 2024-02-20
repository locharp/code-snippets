import java.util.ArrayList;
public class Solution
{

    public static int findPeakElement
    ( ArrayList< Integer > arr )
    {
        int n = arr.size();
        int m = arr.size() - 1;

        if ( n < 2 || arr.get( 0 ) > arr.get( 1 ) )
        {
            return 0;
        }
        else if ( arr.get( m ) > arr.get( m - 1 ) )
        {
            return m;
        }

        for ( int i = 1; i < m; i++ )
        {
            if ( arr.get( i ) > arr.get( i + 1 )
                && arr.get( i ) > arr.get( i - 1 ) )
            {
                return i;
            }
        }

        return -1;
    }

}
