public class Solution
{

    public static boolean isPowerOfTwo
    ( int n )
    {
        if ( n < 1 )
        {
            return false;
        }

        int o = 1;

        while ( o < n )
        {
            o *= 2;
        }

        return n == o;
    }

}
