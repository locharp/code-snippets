import java.util.*;

public class Solution
{
	
	public static ArrayList< Integer > printMatrix
	( int[][] mat, int n, int m )
	{	
		ArrayList< Integer > ans =
		    new ArrayList<>();
		ArrayList< Integer > o =
			new ArrayList<>();
		ans.add( mat[0][0] );
		o.add( 0 );
		o.add( 0 );
		o.add( 0 );
		o.add( 0 );
		n--;
		m--;

		while ( o.get( 0 ) != n || o.get( 1 ) != m )
		{
			if ( o.get( 1 ) == m )
			{
				o.set( 0, o.get( 0 ) + 1 );
				o.set( 2, 1 );
				o.set( 3, -1 );
			}
			else if ( o.get( 0 ) < 1 )
			{
				o.set( 1, o.get( 1 ) + 1 );
				o.set( 2, 1 );
				o.set( 3, -1 );
			}
			else if ( o.get( 0 ) == n )
			{
				o.set( 1, o.get( 1 ) + 1 );
				o.set( 2, -1 );
				o.set( 3, 1 );
			}
			else
			{
				o.set( 0, o.get( 0 ) + 1 );
				o.set( 2, -1 );
				o.set( 3, 1 );
			}
			
			ans.add( mat[ o.get( 0 ) ][ o.get( 1 ) ] );
			o( ans, o, mat );
		}

		return ans;
	}



	static void o
	( ArrayList< Integer > ans,
	  ArrayList< Integer > o,
	  int[][] mat )
	{
		while ( o.get( 0 ) + o.get( 2 ) >= 0
		     && o.get( 0 ) + o.get( 2 )  <= mat.length - 1
		     && o.get( 1 ) + o.get( 3 )  >= 0
			 && o.get( 1 ) + o.get( 3 )  <= mat[0].length - 1 )
		{
			o.set( 0, o.get( 0 ) + o.get( 2 ) );
			o.set( 1, o.get( 1 ) + o.get( 3 ) );
			ans.add( mat[ o.get( 0 ) ][ o.get( 1 ) ] );
		}
	}

}
