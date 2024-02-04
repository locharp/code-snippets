<?php



function pythagorean_triple
( $integers )
{
    sort( $integers );
    $m = pow( $integers[0], 2 );
    $n = pow( $integers[1], 2 );
    $o = pow( $integers[2], 2 );
    
    if ( $m + $n == $o )
    {
        return 1;
    }
    else
    {
        return 0;
    }
}



?>
