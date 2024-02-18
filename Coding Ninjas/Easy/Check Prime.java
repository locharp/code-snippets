public class Solution
{

	public static String isPrime
	( int num )
	{

		if ( num < 2 )
		{
			return "NO";
		}
		
		int n = ( int ) Math.sqrt( num );

		for ( int i = 2; i <= n; i++ )
		{
			if ( num % i < 1 )
			{
				return "NO";
			}
		}

		return "YES";
	}

}
