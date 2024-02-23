public class Solution
{

	public static String nextSmallerPalindrome
	( String s )
	{
		if ( s.equals( "1" ) )
		{
			return "0";
		}

		int n = s.length();
		int m = ( n + 1 ) / 2;
		char[] t = s.substring( 0, m ).toCharArray();
		
		for ( int i = m - 1; i >= 0; i-- )
		{
			if ( t[i] > '0' )
			{
				t[i]--;
				break;
			}
			else
			{
				t[i] = '9';
			}
		}

		if ( t[0] < '1' )
		{
			return "9".repeat( n - 1 );
		}

		String u = new String( t );

		return u + new StringBuilder( u.substring( 0, n - m ) ).reverse().toString();
	}

}
