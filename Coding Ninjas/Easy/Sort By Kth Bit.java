public class Solution
{

    public static int[] sortArrayByKBit( int n, int k, int arr[] )
    {
        int[] p = new int[ n + 1 ];
        int[] q = new int[ n + 1 ];
        int i = 0;
        int j = 0;
        k--;

        for ( int a : arr )
        {
            if ( ( a >> k & 1 ) < 1 )
            {
                p[j++] = a;
            }
            else
            {
                q[i++] = a;
            }
        }

        i = 0;

        for ( int a : p )
        {
            if ( a < 1 )
            {
                break;
            }

            arr[i++] = a;
        }
        
        for ( int a : q )
        {
            if ( a < 1 )
            {
                break;
            }

            arr[i++] = a;
        }

        return arr;
    }
    
}
