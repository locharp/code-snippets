import java.util.stream.*;
class Solution
{

    public static int minimumRateToEatBananas
    ( int []v, int h )
    {
        int i = 1;
        int j = IntStream.of( v ).max().getAsInt();
        
        while ( i < j )
        {
            double k = ( double ) ( ( i + j ) / 2 );
            double m = 0;

            for ( int n : v )
            {
                m += Math.ceil( n / k );
            }

            if ( m > h )
            {
                i = ( int ) k + 1;
            }
            else
            {
                j = ( int ) k;
            }
        }

        return i;
    }

}
