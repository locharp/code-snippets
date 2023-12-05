public class Kata
{
    public static int Mango( int quantity, int price )
    {
        int pack = quantity / 3;
        int loose = quantity - ( pack * 3 );
        int total = ( ( pack * 2 ) + loose ) * price;
        
        return total;
    }
}
