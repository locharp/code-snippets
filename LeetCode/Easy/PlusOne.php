class Solution
{

    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function plusOne( $digits )
    {
        $digits = array_reverse( $digits );
        $digits[0] += 1;
        
        for ( $i = 0; $i < count( $digits ) && $digits[$i] > 9; $i++ )
        {
            $digits[$i] = 0;
            $digits[$i + 1] += 1;
        }
        
        return array_reverse( $digits );
    }
}