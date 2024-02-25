import java.util.*;

public class Solution
{
	
	static ArrayList< Integer > ans;
	static int[][] map;
	static int[][] dir;
	static int d;
	static int m;



	static void changeDir()
	{
		if ( map[ ans.get( 0 ) ][ ans.get( 1 ) ] > 0 )
		{
			d = ( d + 1 ) % dir.length;
		}
		else
		{
			d = ( d - 1 + dir.length ) % dir.length;
		}
	}



	static void move()
	{
		if ( ans.get( 0 ) < 0 || ans.get( 0 ) >= map.length
			|| ans.get( 1 ) < 0 || ans.get( 1 ) >= map[0].length )
		{
			ans.set( 0, -1 );
			ans.set( 1, -1 );

			return;
		}
		else if ( m < 1 )
		{
			return;
		}

		changeDir();
		map[ ans.get( 0 ) ][ ans.get( 1 ) ] =
			1 - map[ ans.get( 0 ) ][ ans.get( 1 ) ];
		ans.set( 0, dir[d][0] + ans.get( 0 ) );
		ans.set( 1, dir[d][1] + ans.get( 1 ) );
		m--;
		move();
	}


	
	public static ArrayList<Integer> ninjaAnt
	( int[][] mat, int sr, int sc, int moves )
	{
		ans = new ArrayList<>();
		ans.add( sr );
		ans.add( sc );
		dir = new int[][] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
		map = mat;
		m = moves;
		d = 0;
		move();
		
		return ans;
	}

}
