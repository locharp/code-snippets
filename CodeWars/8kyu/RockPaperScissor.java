import java.util.ArrayList;
import java.util.Arrays;

public class Kata
{
    public static String rps( String p1, String p2 )
    {
        ArrayList<String> weapons = new ArrayList<String>( Arrays.asList( "rock", "paper", "scisors" ) );
        int result = weapons.indexOf( p1 ) - weapons.indexOf( p2 );
      
        if ( result == -1)
        {
            result = 2;
        }
        else if ( result == -2 )
        {
            result = 1;
        }
    
        if ( result == 0 )
        {
            return "Draw!";
        }
        else
        {
            return "Player " + result + " won!";
        }
    }
}