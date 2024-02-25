public class Solution
{

	static Double convert
	( String s )
	{
		if ( s.endsWith( ")" ) )
		{
			int i = s.indexOf( '(' );
			String s1 = s.substring( 0, i );
			String s2 = s.substring( i + 1, s.length() - 1 );
			String s3 = s1 + s2.repeat( 20 );

			return Double.parseDouble( s3 );
		}
		else
		{
			return Double.parseDouble( s );
		}
	}
	
	
	
	public static boolean isEqual
	( String s, String t )
	{
		return convert( s ).equals( convert( t ) );
	}

}
