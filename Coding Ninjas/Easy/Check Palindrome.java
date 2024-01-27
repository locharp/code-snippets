public class Solution
{

    public static Boolean isPalindrome( String s )
    {
        StringBuilder t = new StringBuilder( s );
        t.reverse();

        return s.equals( t.toString() );
    }
    
}
