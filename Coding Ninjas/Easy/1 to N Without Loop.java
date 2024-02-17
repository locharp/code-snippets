public class Solution
{

    static int[] f( int[] arr, int x )
    {
        if ( x < 1 )
        {
            return arr;
        }

        arr[ x - 1 ] = x;

        return f( arr, x - 1 );
    }


    
    public static int[] printNos
    ( int x )
    {
        int[] ans = new int[x];
        return f( ans, x );
    }
}
