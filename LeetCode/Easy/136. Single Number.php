class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNumber( $nums )
    {
        $nums = array_count_values( $nums );
        
        return array_search( 1, $nums );
    }
}