public class Solution
{
    public int MaxProduct( int[] nums )
    {
        Array.Sort( nums );
        int m = nums[ nums.Length - 1 ] - 1;
        int n = nums[ nums.Length - 2 ] - 1;

        return m * n;
    }
}
