public class Geometry
{
    
    public static double squareArea
    ( double A )
    {
        double r = A * 2 / Math.PI;
        double s = r * r;
        
        return Math.round( s * 100 ) / 100.0;
    }
    
} 
