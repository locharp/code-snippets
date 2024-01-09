import java.util.ArrayList;

class Solution
{
    static int f( ArrayList<Integer> list, int n )
    {
        int i = 0;
        int j = list.size();
        int k = 0;

        while ( i < j )
        {
            k = ( i + j ) / 2;

            if ( list.get( k ) < n )
            {
                i = k + 1;
            }
            else
            {
                j = k;
            }
        }

        return i;
    }
    
    
    
    public static int[] countNumber( int n, int[] arr )
    {
        ArrayList<Integer> list = new ArrayList<>();
        int[] ans = new int[n];
        list.add( arr[ n - 1 ] );
        
        for ( int i = n - 2; i >= 0; i-- )
        {
            int j = f( list, arr[i] );
            ans[i] = j;
            list.add( j, arr[i] );
        }

        return ans;
    } 
}
