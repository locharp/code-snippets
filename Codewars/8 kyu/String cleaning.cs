public class Kata
{
    public static string StringClean( string s )
    {
        string numbers = "1234567890";
        string ans = "";
        
        foreach ( char ch in s )
        {
            if ( !numbers.Contains( ch ) )
            {
                ans += ch;
            }
        }
        
        return ans;
    }
}
