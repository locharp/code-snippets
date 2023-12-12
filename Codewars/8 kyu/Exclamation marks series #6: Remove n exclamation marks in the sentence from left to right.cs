using System.Text.RegularExpressions;

public class Kata
{
  public static string Remove( string s, int n )
  {
      Regex rg = new Regex( "!" );
      
      return rg.Replace( s, "", n );
  }
}
