public class Solution
{

    static int solve
    ( String s )
    {
        int ans = 1;
        int curr = 1;
        boolean t = true;

        for ( int i = 1; i < s.length(); i++ )
        {
            if ( s.charAt( i ) > s.charAt( i - 1 ) )
            {
                if ( t )
                {
                    curr++;
                    ans = Math.max( curr, ans );
                }
                else
                {
                    t = true;
                    curr = 2;
                }
            }
            else if ( s.charAt( i ) < s.charAt( i - 1 ) )
            {
                if ( t )
                {
                    t = false;
                    curr = 2;
                }
                else
                {
                    curr++;
                    ans = Math.max( curr, ans );
                }
            }
            else
            {
                curr = 1;
            }
        }


        return ans;
    }

}
