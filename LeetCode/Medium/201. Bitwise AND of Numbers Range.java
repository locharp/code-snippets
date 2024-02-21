class Solution
{

    public int rangeBitwiseAnd
     (int left, int right )
    {
        int ans = right;

        for ( int i = left; i < right && ans > 0; i++ )
        {
            ans &= i;
        }

        return ans;
    }

}
