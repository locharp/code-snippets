class Solution
{

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit( $prices )
    {
        $profit = 0;
        
        foreach ( array_slice( $prices, 1 ) as $day => $price )
        {
            if ( $price > $prices[$day] )
            {
                $profit += $price - $prices[$day];
            }
        }
        
        return $profit;
    }
}