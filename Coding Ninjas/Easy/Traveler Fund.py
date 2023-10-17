public class Solution
{
    public static int travelerFund( int[] a )
    {
        int min = 0, curr = 1;

        for ( int i : a )
        {
            curr -= i;
            min = Math.max( min, curr );
        }

        return min;
    }
}
