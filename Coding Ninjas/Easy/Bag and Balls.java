public class Solution
{

    static int numberOfRemovals
    ( int n, String s )
    {
        int ans = 0;
        int i = 0;
        

        for ( char ch : s.toCharArray() )
        {
            if ( ch == '1' )
            {
                i++;
            }
            else if ( i > 0 )
            {
                i--;
                ans++;
            }
        }


        return ans;
    }

}
