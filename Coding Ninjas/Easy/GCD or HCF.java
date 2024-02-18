public class Solution
{

    public static int calcGCD( int n, int m )
    {
        if ( n < 1 )
        {
            return m;
        }

        return calcGCD( m % n, n );
    }

}
