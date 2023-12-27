<?php



class Solution
{
    function minCost( $colors, $neededTime )
    {
        $ans = 0;
        $n = strlen( $colors );
        
        for ( $i = 0; $i < $n; )
        {
            if ( $colors[$i] != $colors[ $i - 1 ] )
            {
                $i++;
                continue;
            }
            
            $a = array( $neededTime[ $i - 1 ] );
            
            while ( $i < $n && 
                   $colors[ $i ] == $colors[ $i - 1 ] )
            {
                array_push( $a, $neededTime[$i++] );
            }
            
            rsort( $a );
            $ans += array_sum( array_slice( $a, 1 ) );
        }
        
        return $ans;
    }
}



?>
