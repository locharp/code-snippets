import java.util.*;

public class Solution
{

    public static double maximumValue
	( Pair[] items, int n, int w )
	{
		double ans = 0;
		Arrays.sort( items, ( x, y ) ->
			Double.compare( ( double ) y.value / y.weight, ( double ) x.value / x.weight ) );
		
		for ( Pair item : items )
		{
			if ( w < item.weight )
			{
				ans += ( double ) item.value / item.weight * w;
				w = 0;
			}
			else
			{
				ans += item.value;
				w -= item.weight;
			}

			if ( w < 1 )
			{
				break;
			}
		}
		
		return ans;
    }

}
