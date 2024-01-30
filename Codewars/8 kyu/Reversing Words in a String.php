<?php



function reverse
( $string )
{
    $a = explode( " ", $string );
    $a = array_reverse( $a );
    
    return join( " ", $a );
}



?>
