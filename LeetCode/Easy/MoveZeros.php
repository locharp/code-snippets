class Solution
{

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function moveZeroes( &$nums )
    {
        $nums = array_pad( array_diff( $nums, [ 0 ] ), count( $nums ), 0 ); 
    }
}