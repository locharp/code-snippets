public class Kata
{
    public static boolean validateHello( String greetings )
    {
        String[] a = { "hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc" };
        greetings = greetings.toLowerCase();
        
        for ( String s : a )
        {
            if ( greetings.contains( s ) )
            {
                return true;
            }
        }
        
        return false;
    }
}
