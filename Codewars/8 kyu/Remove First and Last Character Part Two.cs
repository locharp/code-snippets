using System;

public static class Kata
{
    public static string Array( string s )
    {
        string[] a = s.Split( "," );
        
        if ( a.Length < 3 )
        {
            return null;
        }
        
        return string.Join( " ", a[ 1..( a.Length - 1 ) ] );
    }
}
