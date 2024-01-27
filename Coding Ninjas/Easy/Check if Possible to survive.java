public class Solution
{

    public static Boolean isPossibleToSurvive( int n, int x, int d )
    {
        if ( x > n )
        {
            return false;
        }
        else if ( d > 6 && x * 7 > n * 6 )
        {
            return false;
        }
        else
        {
            return true;
        }
    }

}
