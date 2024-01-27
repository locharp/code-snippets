import java.lang.Character;

public class Solution
{
	
	public static int goodnessOfString( String s )
	{
		int ans = 0;
		int k = 0;
		int MOD = 1000000007;

		for ( int i = 0; i < s.length(); i++ )
		{
			if ( Character.isDigit( s.charAt( i ) ) )
			{
				long j = 0;

				while ( Character.isDigit( s.charAt( i ) ) )
				{
					j = ( j * 10 ) + ( Character.getNumericValue( s.charAt( i++ ) ) );
				}
				
				j = ( j * k ) % MOD;
				ans = ( ans + ( int ) j ) % MOD;
				i--;
			}
			else if ( s.charAt( i ) == '[' )
			{
				k++;
			}
			else if ( s.charAt( i ) == ']' )
			{
				k--;
			}
		}

		return ans;
	}

}
