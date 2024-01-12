import java.util.*;

public class Solution
{
    
    public static String maximumDifference( int n, int[] arr )
    {
        Arrays.sort( arr );
        int diff = arr[ arr.length - 1 ] - arr[0];
        
        if ( diff % 2 == 0 )
        {
            return "EVEN";
        }
        else
        {
            return "ODD";
        }
    }
    
}
