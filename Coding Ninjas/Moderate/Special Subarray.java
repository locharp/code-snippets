import java.util.*;

public class Solution
{

	public static int[] specialSubarray( int n, int[] arr )
	{
		int i = 0;
		int j = 0;
		int k = 0;
		int p = 0;
		int q = n;
		ArrayList<Integer> m = new ArrayList<>();
		HashMap< Integer, Integer > c = new HashMap<>();
		HashMap< Integer, AbstractMap.SimpleEntry< Integer, Integer > > d = new HashMap<>();
		
		for ( ; i < n; i++ )
		{
			if ( c.containsKey( arr[i] ) )
			{
				j = c.get( arr[i] );
				c.put( arr[i], j + 1 );
				d.get( arr[i] ).setValue( i );
			}
			else
			{
				c.put( arr[i], 1 );
				d.put( arr[i], new AbstractMap.SimpleEntry<>( i, i ) );
			}

			if( c.get( arr[i] ) == k )
			{
				m.add( arr[i] );
			}
			else if ( c.get( arr[i] ) > k )
			{
				m.clear();
				m.add( arr[i] );
				k = c.get( arr[i] );
			}
		}
		
		for ( Integer o : m )
		{
			i = d.get( o ).getKey();
			j = d.get( o ).getValue();
			
			if ( j - i < q - p )
			{
				p = i;
				q = j;
			}
		}
		
		return Arrays.copyOfRange( arr, p, q + 1 );
	}

}
