class Solution
{

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function intersect( $nums1, $nums2 )
    {
        $nums1 = array_count_values( $nums1 );
        $nums2 = array_count_values( $nums2 );
        $intersect = array();
        
        foreach ( $nums1 as $index => $num )
        {
            if ( array_key_exists( $index, $nums2 ) )
            {
                $intersect = array_merge( $intersect, array_fill( 0, min( $nums2[$index], $num ), $index ) );
            }
        }
        
        return $intersect;
    }
}