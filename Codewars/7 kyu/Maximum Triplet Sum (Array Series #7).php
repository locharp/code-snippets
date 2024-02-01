<?php



function maxTriSum
( $nums )
{
    $nums = array_unique( $nums );
    rsort( $nums );
    
    return array_sum( array_slice( $nums, 0, 3 ) );
}



?>
