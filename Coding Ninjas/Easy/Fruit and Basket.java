import java.util.*;
import java.util.AbstractMap.*;

public class Solution
{

    public static int findMaxFruits
    ( int []arr, int n )
    {
        ArrayList< SimpleEntry< Integer, Integer > > list =
            new ArrayList<>();
        Integer i = -1;
        Integer curr = 0;
        Integer prev = 0;
        int count = 0;
        int ans = 1;
        
        for ( Integer num : arr )
        {
            if ( num.equals( curr ) )
            {
                list.get( i ).setValue( list.get( i ).getValue() + 1 );
            }
            else
            {
                curr = num;
                list.add( new SimpleEntry<>( num, 1 ) );
                i++;
            }
        }
        
        for ( ; i > 0; i-- )
        {
            curr = list.get( i ).getKey();
            prev = list.get( i - 1 ).getKey();
            count = 0;

            for ( int j = i; j >= 0; j-- )
            {
                Integer k = list.get( j ).getKey();

                if ( k == curr || k == prev )
                {
                    count += list.get( j ).getValue();
                }
                else
                {
                    break;
                }
            }

            ans = Math.max( count, ans );
        }

        return ans;
    }
    
}
