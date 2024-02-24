import java.util.* ;

public class Solution
{

	public static ArrayList< Integer > findAnagramsIndices
	( String str, String ptn, int n, int m )
	{
		ArrayList< Integer > ans = new ArrayList<>();
		HashMap< Character, Integer > map1 = new HashMap<>();
		HashMap< Character, Integer > map2 = new HashMap<>();
		char[] s = str.toCharArray();

		for ( int i = 0; i < m; i++ )
		{
			map1.put( ptn.charAt( i ), map1.getOrDefault( ptn.charAt( i ), 0 ) + 1 );
			map2.put( s[i], map2.getOrDefault( s[i], 0 ) + 1 );
		}

		if ( map1.equals( map2 ) )
		{
			ans.add( 0 );
		}

		for ( int i = 0, j = m; j < n; i++, j++ )
		{
			if ( map2.get( s[i] ).equals( 1 ) )
			{
				map2.remove( s[i] );
			}
			else
			{
				map2.put( s[i], map2.get( s[i] ) - 1 );
			}

			map2.put( s[j], map2.getOrDefault( s[j], 0 ) + 1 );

			if ( map1.equals( map2 ) )
			{
				ans.add( i + 1 );
			}
		}

		return ans;
	}

}
