public class Kata
{
    public static double Billboard( string name, double price = 30 )
    {
        double total = 0;
        
        foreach ( char ch in name )
        {
            total += price;
        }
        
        return total;
    }
}
