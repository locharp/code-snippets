public class Solution
{

    static boolean isKthBitSet
    ( int n, int k )
    {
        String s = Integer.toBinaryString( n );

        return s.charAt( s.length() - k ) == '1';
    }
    
}
