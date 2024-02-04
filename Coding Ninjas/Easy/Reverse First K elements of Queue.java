import java.util.*;

public class Solution 
{
    
    public static Queue< Integer > reverseElements
    ( Queue< Integer > q, int k ) 
    {
        f( q, k );
        for ( int i = k; i < q.size(); i++ )
        {
            q.offer( q.poll() );
        }
        
        return q;
    }



    static void f( Queue< Integer > q, int k )
    {
        if ( k < 1 )
        {
            return;
        }

        int t = q.poll();
        f( q, k - 1 );
        q.offer( t );
    }

}
