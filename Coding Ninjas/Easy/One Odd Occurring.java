import java.util.*;

public class Solution
{

    public static int missingNumber
    ( int n, int []arr )
    {
        HashSet< Integer > set =
            new HashSet<>();
        Integer ans = 0;

        for ( int num : arr )
        {
            if ( set.contains( num ) )
            {
                set.remove( num );
            }
            else
            {
                set.add( num );
            }
        }

        for ( Integer num : set )
        {
            ans = num;
        }

        return ans;
    }

}
