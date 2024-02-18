import java.util.*;

public class Solution
{

    static HashMap< String, TreeSet< Integer > > map =
        new HashMap<>();
    
    public static void receiveMessage
    ( String user, int time )
    {   
        if ( !map.containsKey( user ) )
        {
            map.put( user, new TreeSet<>() );
        }

        map.get( user ).add( time );
    }



 	public static ArrayList< Integer > getMessageCount
    ( int l, int r, String user, int k )
    {
    	ArrayList< Integer > ans =
            new ArrayList<>();
        TreeSet< Integer > s = map.get( user );
        
        for ( int i = l; i <= r; i += k )
        {
            ans.add( s.subSet( i, Math.min( i + k, r + 1 ) ).size() );
        }

        return ans;
    }
       
}
