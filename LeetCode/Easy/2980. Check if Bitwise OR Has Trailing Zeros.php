<?php



class Solution
{

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    
    function hasTrailingZeros( $nums )
    {
        for ( $i = 0; $i < count( $nums ); $i++ )
        {
            foreach ( array_slice( $nums, $i + 1 ) as $j )
            {
                if ( ( $nums[$i] | $j )  % 2 < 1 )
                {
                    return TRUE;
                }
            }
        }
        
        return FALSE;
    }
}



?>
