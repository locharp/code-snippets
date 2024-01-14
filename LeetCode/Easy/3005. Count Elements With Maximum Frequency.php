<?php



class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    
    function maxFrequencyElements( $nums )
    {
        $a = array_count_values( $nums );
        rsort( $a );
        $ans = $m = $a[0];
        
        foreach ( array_slice( $a, 1 ) as $i )
        {
            if ( $i < $m )
            {
                break;
            }
            
            $ans += $i;
        }
        
        return $ans;
    }
}



?>
