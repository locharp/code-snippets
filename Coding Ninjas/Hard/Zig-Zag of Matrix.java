import java.util.*;

public class Solution
{
	
	public static ArrayList< Integer > printMatrix
	( int[][] mat, int n, int m )
	{	
		ArrayList< Integer > ans =
		    new ArrayList<>();
		ans.add( mat[0][0] );
		int i = 0;
		int j = 0;
		int p = 0;
		int q = 0;
		n--;
		m--;

		while ( i != n || j != m )
		{
			if ( j == m )
			{
				i++;
				p = 1;
				q = -1;
			}
			else if ( i < 1 )
			{
				j++;
				p = 1;
				q = -1;
			}
			else if ( i == n )
			{
				j++;
				p = -1;
				q = 1;
			}
			else
			{
				i++;
				p = -1;
				q = 1;
			}
			
			ans.add( mat[i][j] );
			
			while ( i + p >= 0
				 && i + p  <= n
				 && j + q  >= 0
				 && j + q  <= m )
			{
				i += p;
				j += q;
				ans.add( mat[i][j] );
			}
		}

		return ans;
	}
	
}
