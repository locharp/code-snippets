public class Solution
{

    public static int findProductSumDifference
    ( int n )
    {
        int p = 1;
        int q = 0;

        while ( n > 0 )
        {
            int o = n % 10;
            n /= 10;
            p *= o;
            q += o;
        }

        return p - q;
    }

}
