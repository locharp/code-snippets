import java.util.*;

public class Solution
{
    static ArrayList<Integer> jumpsOnMatrix( int n, int m, int x, int y, ArrayList< ArrayList<Integer> > a )
    {
        ArrayList<Integer> ans = new ArrayList<>();

        for ( int i = 0, j = 0; i < n && j < m; i += y, j += x )
        {
            ans.add( a.get( i ).get( j ) );
        }

        return ans;
    }
}
