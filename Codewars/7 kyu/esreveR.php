<?php



function reverse
( array $a ): array
{
    $ans = array();
    
    foreach ( $a as $i )
    {
        array_unshift( $ans, $i );
    }
    
    return $ans;
}



?>
