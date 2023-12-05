/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame
{
    public int GuessNumber( int n )
    {
        int i = 1;

        while ( i < n )
        {
            int j = i + ( ( n - i ) / 2 );
            int k = guess( j );
            Console.WriteLine( $"{i} {j} {n} {k}");
            if ( k > 0 )
            {
                i = j + 1;
            }
            else
            {
                n = j;
            }
        }

        return i;
    }
}
