import java.util.ArrayList;
import java.util.stream.Collectors; 

public class Solution
{

	public static int calculateScore( ArrayList<String> matchResult, int n )
	{
		ArrayList<Integer> list = new ArrayList<>();

		for ( String s : matchResult )
		{
			switch ( s )
			{
				case "+":
					list.add( list.get( list.size() - 2 ) + list.get( list.size() - 1 ) );
					break;
				case "C":
					list.remove( list.size() - 1 );
					break;
				case "D":
					list.add( list.get( list.size() - 1 ) * 2 );
					break;
				default:
					list.add( Integer.parseInt( s ) );
			}
		}

		return list.stream().collect( Collectors.summingInt( Integer::intValue ) );
		
	}
}

