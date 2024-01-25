import java.util.Arrays;

public class Solution
{
    
    public static int[] termsOfAP( int x )
    {
        int[] ans = new int[x];
        
        for ( int i = 0, j = 1, k = 0; i < x; i++ )
        {
            do
            {
                k = j++ * 3 + 2;

                if ( k % 4 > 0 )
                {
                    ans[i] = k;
                    break;
                }
            }
            while( true );
        }
        
        return Arrays.copyOfRange( ans, 0, x );
    }
    
}
