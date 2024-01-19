public class Solution
{
    public static int findMin( int []arr )
    {
        int i = 0;

        for ( int j = arr.length - 1; i < j ; )
        {
            int k = ( i + j ) / 2;

            if ( arr[j] > arr[k] )
            {
                j = k;
            }
            else
            {
                i = k + 1;
            }
        }

        return arr[i];
    }
}
