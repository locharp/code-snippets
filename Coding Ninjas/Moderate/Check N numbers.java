public class Solution
{
    public static int getNewNum( ArrayList<Integer> arr, int n )
    {
        int[] a = new int[13];
        int ans = 0;
        for ( int i : arr )
        {
            int j = 0;
            
            while ( i > 0 )
            {
                a[j] += i & 1;
                i >>= 1;
                j++;
            }
        }
        
        for ( int i = 0; i < 13; i++ )
        {
            if ( a[i] > n / 2 )
            {
                ans |= (1 << i);
            }
        }
        
        return ans;
    }
}
