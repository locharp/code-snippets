import java.util.*;

public class Solution {

    public static int getNewNum(ArrayList<Integer> arr, int n) {

        int m = n / 2;
        int ans = 0;
        
        for ( int i = 0; i < 13; i++ )
        {
            int count = 0;

            for ( Integer j : arr )
            {
                count += ( j >> i ) & 1;
            }

            if ( count > m )
            {
                ans |= 1 << i;
            }
        }

        return ans;
    }
}
