import java.util.*;

public class Solution
{

	public static Integer coverageOfMatrix
	( ArrayList< ArrayList< Integer > > mat )
	{
		Integer ans = 0;

		for ( int i = 0; i < mat.size(); i++ )
		{
			for ( int j = 0; j < mat.get( i ).size(); j++ )
			{
				if ( mat.get( i ).get( j ) < 1 )
				{
					if ( i > 0 )
					{
						ans += mat.get( i - 1 ).get( j );
					}

					if ( i < mat.size() - 1 )
					{
						ans += mat.get( i + 1 ).get( j );
					}

					if ( j > 0 )
					{
						ans += mat.get( i ).get( j - 1 );
					}

					if ( j < mat.get( i ).size() - 1 )
					{
						ans += mat.get( i ).get( j + 1 );
					}
				}
			}
		}

		return ans;
	}

}
