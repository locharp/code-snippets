import java.util.*;

public class Solution
{
    static int copyPaste( int n, ArrayList<Integer> a, int x, int k )
    {
        if ( ( a.indexOf( x ) + 1 ) % n == k % n )
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
}
