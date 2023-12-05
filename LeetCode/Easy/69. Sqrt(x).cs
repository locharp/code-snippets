public class Solution
{
    public int MySqrt( int x )
    {
        if ( x < 2 )
        {
            return x;
        }

        int i = 0, j = x;

        while ( i < j )
        {
            int k = i + ( ( j - i ) / 2 );
            
            if ( x / k < k )
            {
                j = k;
            }
            else
            {
                i = k + 1;
            }
        }

        return i - 1;
    }
}
