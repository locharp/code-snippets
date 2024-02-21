import java.util.ArrayList;

public class Solution
{

	static boolean f
	( ArrayList< ArrayList< Integer > > arr, int i, int j )
	{
		Integer k = 0;

		for ( int m = 0; m < arr.size(); m++ )
		{
			k += arr.get( i ).get( m ) * arr.get( m ).get( j );
		}

		return k.equals( arr.get( i ).get( j ) );
	}

	public static boolean matrixGame
	( ArrayList< ArrayList< Integer > > arr )
	{
		for ( int i = 0; i < arr.size(); i++ )
		{
			for ( int j = 0; j < arr.size(); j++ )
			{
				if ( !f( arr, i, j ) )
				{
					return false;
				}
			}
		}

		return true;
	}

}
