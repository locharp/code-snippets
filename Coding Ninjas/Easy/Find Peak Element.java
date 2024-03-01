import java.util.ArrayList;

public class Solution
{
    public static int findPeakElement
    ( ArrayList< Integer > arr )
    {
        int j = arr.size() - 1;
        int i = 1;

        if ( j < 1 || arr.get( 0 ) > arr.get( 1 ) )
        {
            return 0;
        }
        else if ( arr.get( j ) > arr.get( j - 1 ) )
        {
            return j;
        }
        
        while ( i < j )
        {
            int k = ( i + j ) / 2;

            if ( arr.get( k ) > arr.get( k - 1 ) )
            {
                if ( arr.get( k ) > arr.get( k + 1 ) )
                {
                    i = k;
                    j = k;
                }
                else
                {
                    i = k + 1;
                }
            }
            else
            {
                j = k - 1;
            }
        }
        
        return i;
    }

}
