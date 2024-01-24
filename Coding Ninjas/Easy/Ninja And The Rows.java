import java.util.Arrays;
import java.util.Comparator;

public class Solution
{

    public static int maximumWeightRow( int n, int m, int[][] mat )
    {
        return Arrays.stream( mat ).map( row -> Arrays.stream( row ).sum() ).max( Integer::compare ).get();
    }
    
}
