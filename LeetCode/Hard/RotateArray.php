class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return NULL
     */
    function rotate( &$nums, $k )
    {
        $count = count( $nums );
        $k %= $count;
        
        if ( $k == 0 )
        {
            return;
        }
     
        $nums = array_merge( array_slice( $nums, -$k ), array_slice( $nums, 0, $count - $k ) );
    }
}