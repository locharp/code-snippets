import java.util.* ;

public class Solution
{

	public static ArrayList< Integer > findAnagramsIndices
	( String str, String ptn, int n, int m )
	{
		ArrayList< Integer > ans = new ArrayList<>();
		char[] s = str.toCharArray();
		char[] t = ptn.toCharArray();
		Arrays.sort( t );
		int o = t.length;
		int p = s.length - o;

		for ( int i = 0; i <= p; i++ )
		{
			char[] r = Arrays.copyOfRange( s, i, i + o );
			Arrays.sort( r );
			
			if ( Arrays.equals( r, t ) )
			{
				ans.add( i );
			}
		}

		return ans;
	}

}
