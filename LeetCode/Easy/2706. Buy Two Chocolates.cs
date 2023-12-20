public class Solution
{
    public int BuyChoco( int[] prices, int money )
    {
        if ( prices.Length < 2 )
        {
            return money;
        }
        
        Array.Sort( prices );
        int two = prices[0] + prices[1];

        if ( money >= two )
        {
            money -= two;
        }

        return money;
    }
}
