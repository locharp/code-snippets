import java.util.*;

public class Solution
{

	public static int getLongestSubarray
	( int []nums, int k )
	{
		HashMap< Integer, Integer > map =
			new HashMap<>();
		map.put( 0, -1 );
		int ans = 0;
		int sum = 0;
		int diff = 0;

		for ( int i = 0; i < nums.length; i++ )
		{
			sum += nums[i];
			diff = sum - k;

			if ( map.containsKey( diff ) )
			{
				ans = Math.max( i - map.get( diff ), ans );
			}

			if ( !map.containsKey( sum ) )
			{
				map.put( sum, i );
			}
		}
		
		return ans;
	}

}
