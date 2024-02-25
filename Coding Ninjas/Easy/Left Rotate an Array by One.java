public class Solution
{
    
    static int[] rotateArray
    ( int[] arr, int n )
    {
        int temp = arr[0];
        n--;

        for ( int i = 0; i < n; i++ )
        {
            arr[i] = arr[ i + 1 ];
        }

        arr[n] = temp;

        return arr;
    }

}
