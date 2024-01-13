<?php



class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer
     */

    function minOperations( $nums )
    {
        $a = array_count_values( $nums );
        $ans = 0;
        
        foreach ( $a as $i => $j )
        {
            if ( $j < 2 )
            {
                return -1;
            }

            $ans += ceil( $j / 3 );
        }

        return $ans;
    }
  
}



?>
