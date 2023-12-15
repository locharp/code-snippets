using System;

public class GpsSpeed
{    
    public static int Gps( int s, double[] x )
    {
        double m = 0;
        
        for ( int i = 1; i < x.Length; i++ )
        {
            m = Math.Max( m, x[i] - x[ i - 1 ] );
        }
        
        return ( int ) Math.Floor( m * 3600 / s );
    }
}
