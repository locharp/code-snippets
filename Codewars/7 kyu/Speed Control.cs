using System;

public class GpsSpeed
{    
    public static int Gps( int s, double[] x )
    {
        double m = 0;
        double n = 0;
      
        for ( int i = 1; i < x.Length; i++ )
        {
            n = x[i] - x[ i - 1 ];
            m = Math.Max( m, n );
        }
        
        return ( int ) Math.Floor( m * 3600 / s );
    }
}
