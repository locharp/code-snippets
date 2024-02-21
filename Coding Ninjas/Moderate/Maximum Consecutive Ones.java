import java.util.ArrayList;

public class Solution
{

	public static int longestSubSeg
	( ArrayList< Integer > arr , int n, int k )
	{
		int ans = 0;

		for ( int i = 0, j = 0, o = 0; j < n; j++ )
		{
			o += 1 - arr.get( j );

			while ( o > k )
			{
				o -= 1 - arr.get( i++ );
			}

			ans = Math.max( j - i, ans );
		}

		return ans + 1;
	}

}
