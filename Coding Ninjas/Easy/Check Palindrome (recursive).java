public class Solution
{

    static boolean isPalindrome
    ( String s, int i )
    {
        if ( i > ( s.length() - 1 ) / 2 )
        {
            return true;
        }
        
        if ( s.charAt( i ) != s.charAt( s.length() - i - 1 ) )
        {
            return false;
        }

        return isPalindrome( s, i + 1 );
    }
    
    
    
    public static boolean isPalindrome
    ( String str )
    {
        return isPalindrome( str, 0 );
    }

}



// Not recursive
public class Solution
{

    public static boolean isPalindrome
    ( String str )
    {
        int n = str.length() - 1;

        for ( int i = 0; i <= str.length() / 2 ; i++ )
        {
            if ( str.charAt( i ) != str.charAt( n - i ) )
            {
                return false;
            }
        }

        return true;
    }

}
