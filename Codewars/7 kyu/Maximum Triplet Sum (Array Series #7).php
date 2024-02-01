<?php



function maxTriSum
( $nums )
{
    $nums = rsort( array_unique( $nums ) );
    
    return array_sum( array_slice( $nums, 0, 3 ) );
}



?>
