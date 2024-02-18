import java.util.*;  

public class Solution
{

	public static int pickCoupons
	( int n, int[] coupons )
	{
	 	int ans = n;
		HashMap< Integer, Integer > map =
			new HashMap<>();
		
		for ( int i = 0; i < n; i++ )
		{
			if ( map.containsKey( coupons[i] ) )
			{
				ans = Math.min( i - map.get( coupons[i] ), ans );
			}

			map.put( coupons[i], i );
		}

		if ( ans == n )
		{
			return -1;
		}
		else
		{
			return ans + 1;
		}
	}

}
