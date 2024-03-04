public class Solution
{

	public static int baseConversion
	( String num, int base )
	{
		try
		{
			return Integer.parseInt( num, base );
		}
		catch ( NumberFormatException e )
		{
			return -1;
		}
	}

}
