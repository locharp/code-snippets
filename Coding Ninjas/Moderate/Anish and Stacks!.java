import java.util.*;

public class Solution
{

    public static int[] k_stack
    ( int l, int n, int q, int[][] queries )
    {
        HashMap< Integer, Stack< Integer > > map =
            new HashMap<>();
        int[] ans = new int[q];
        
        for ( int i = 0; i < q; i++ )
        {
            int o = queries[i][0];
            int p = queries[i][1];

            if ( o < 2 )
            {
                if ( l < 1 )
                {
                    continue;
                }
                else if ( !map.containsKey( p ) )
                {
                    map.put( p, new Stack<>() );
                }

                map.get( p ).push( queries[i][2] );
                l--;
            }
            else
            {
                if ( !map.containsKey( p ) || map.get( p ).isEmpty() )
                {
                    ans[i] = -1;
                }
                else
                {
                    ans[i] = map.get( p ).pop();
                    l++;
                }
            }
        }

        return ans;
    }

}
