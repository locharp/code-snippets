<?php



function solve( $arr )
{
    $a = array();
    
    foreach ( $arr as $i => $j )
    {
        $a[$j] = $i;
    }
    
    asort( $a );
    
    return array_keys( $a );
}



?>
